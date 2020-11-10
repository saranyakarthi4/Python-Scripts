/* Welcome to the SQL mini project. You will carry out this project partly in
the PHPMyAdmin interface, and partly in Jupyter via a Python connection.

This is Tier 2 of the case study, which means that there'll be less guidance for you about how to setup
your local SQLite connection in PART 2 of the case study. This will make the case study more challenging for you: 
you might need to do some digging, aand revise the Working with Relational Databases in Python chapter in the previous resource.

Otherwise, the questions in the case study are exactly the same as with Tier 1. 

PART 1: PHPMyAdmin
You will complete questions 1-9 below in the PHPMyAdmin interface. 
Log in by pasting the following URL into your browser, and
using the following Username and Password:

URL: https://sql.springboard.com/
Username: student
Password: learn_sql@springboard

The data you need is in the "country_club" database. This database
contains 3 tables:
    i) the "Bookings" table,
    ii) the "Facilities" table, and
    iii) the "Members" table.

In this case study, you'll be asked a series of questions. You can
solve them using the platform, but for the final deliverable,
paste the code for each solution into this script, and upload it
to your GitHub.

Before starting with the questions, feel free to take your time,
exploring the data, and getting acquainted with the 3 tables. */


/* QUESTIONS 
/* Q1: Some of the facilities charge a fee to members, but some do not.
Write a SQL query to produce a list of the names of the facilities that do. */
SELECT DISTINCT
CASE WHEN name LIKE '% 1'
THEN REPLACE( name, ' 1', '' )
WHEN name LIKE '% 2'
THEN REPLACE( name, ' 2', '' )
ELSE name
END AS name
FROM `Facilities`
LIMIT 0 , 30


/* Q2: How many facilities do not charge a fee to members? */
SELECT facid, name
FROM `Facilities`
WHERE membercost =0

/* Q3: Write an SQL query to show a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost.
Return the facid, facility name, member cost, and monthly maintenance of the
facilities in question. */
SELECT `facid` , `name` , `membercost` ,`monthlymaintenance`
FROM `Facilities`
WHERE membercost < monthlymaintenance * 0.2
LIMIT 0 , 30


/* Q4: Write an SQL query to retrieve the details of facilities with ID 1 and 5.
Try writing the query without using the OR operator. */
SELECT *
FROM `Facilities`
WHERE facid
IN ( 1, 5 )
LIMIT 0 , 30


/* Q5: Produce a list of facilities, with each labelled as
'cheap' or 'expensive', depending on if their monthly maintenance cost is
more than $100. Return the name and monthly maintenance of the facilities
in question. */
SELECT facid, name,
CASE WHEN `monthlymaintenance` >100
THEN 'Expensive'
ELSE 'Cheap'
END AS fac_label
FROM `Facilities`
GROUP BY 1 , 2, 3
LIMIT 0 , 30

/* Q6: You'd like to get the first and last name of the last member(s)
who signed up. Try not to use the LIMIT clause for your solution. */
select firstname,surname
FROM
(SELECT *,
row_number() over (partition by memid order by joindate desc) as row_num
FROM `Members` WHERE 1
) temp
where row_num = 1


/* Q7: Produce a list of all members who have used a tennis court.
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */
SELECT CONCAT( m.firstname, ' ', m.surname ) name, f.name
FROM `Bookings` b
JOIN (

SELECT facid, name
FROM `Facilities`
WHERE name LIKE 'Tennis Court%'
)f ON b.facid = f.facid
JOIN `Members` m ON b.memid = m.memid
GROUP BY 1 , 2
ORDER BY 1 , 2


/* Q8: Produce a list of bookings on the day of 2012-09-14 which
will cost the member (or guest) more than $30. Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */

SELECT CASE WHEN CONCAT( m.firstname, ' ', m.surname ) LIKE 'GUEST%'
THEN 'GUEST'
ELSE CONCAT( m.firstname, ' ', m.surname )
END AS name, f.facid, f.name AS fac_name
FROM `Bookings` b
JOIN `Facilities` f ON b.facid = f.facid
JOIN `Members` m ON b.memid = m.memid
WHERE CAST( b.starttime AS DATE ) = CAST( '2012-09-14' AS DATE )
AND (
f.membercost >30
OR f.guestcost >30
)
GROUP BY 1 , 2, 3

/* Q9: This time, produce the same result as in Q8, but using a subquery. */
SELECT CASE WHEN CONCAT( m.firstname, ' ', m.surname ) LIKE 'GUEST%'
THEN 'GUEST'
ELSE CONCAT( m.firstname, ' ', m.surname )
END AS name, f.facid, f.name AS fac_name
FROM (

SELECT *
FROM `Bookings`
WHERE CAST( starttime AS DATE ) = CAST( '2012-09-14' AS DATE )
)b
JOIN (

SELECT *
FROM `Facilities`
WHERE (
membercost >30
OR guestcost >30
)
)f ON b.facid = f.facid
JOIN `Members` m ON b.memid = m.memid
GROUP BY 1 , 2, 3
LIMIT 0 , 30

/* PART 2: SQLite

Export the country club data from PHPMyAdmin, and connect to a local SQLite instance from Jupyter notebook 
for the following questions.  

QUESTIONS:
/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */
SELECT b.facid, SUM( (
mems * membercost
) + ( guests * guestcost ) ) AS total_revenue
FROM (
SELECT facid, COUNT( DISTINCT
CASE WHEN memid <>0
THEN memid
END ) mems, COUNT( DISTINCT
CASE WHEN memid =0
THEN memid
END ) guests
FROM `Bookings`
GROUP BY 1
)b
JOIN `Facilities` f ON b.facid = f.facid
GROUP BY 1
HAVING total_revenue <1000
ORDER BY 2
LIMIT 0 , 30

/* Q11: Produce a report of members and who recommended them in alphabetic surname,firstname order */
SELECT m1.firstname, m2.surname, m1.recommendedby, CONCAT( m2.firstname, ' ', m2.surname ) AS recommendedby
FROM Members m1
JOIN Members m2 ON m1.recommendedby = m2.memid
WHERE m2.firstname NOT LIKE '%GUEST%'
GROUP BY 1 , 2, 3, 4
ORDER BY 2 , 1


/* Q12: Find the facilities with their usage by member, but not guests */
SELECT b.facid, m.firstname, b.usages
FROM (

SELECT facid, memid, COUNT( * ) AS usages
FROM Bookings
WHERE memid <>0
GROUP BY 1 , 2
)b
JOIN Members m ON b.memid = m.memid


/* Q13: Find the facilities usage by month, but not guests */
select b.facid, f.name, b.usage_month,b.usages
from
(SELECT facid, SUBSTR( `starttime` , 1, 7 ) AS usage_month, COUNT( * ) AS usages
FROM Bookings
WHERE memid <>0
GROUP BY 1 , 2
) b
join Facilities f ON b.facid = f.facid
order by 1,3
