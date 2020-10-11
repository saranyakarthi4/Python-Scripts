import re
def fun(s):
    # return True if s is a valid email, else return False
  pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
  return (pattern.match(s))

def filter_mail(emails):
    return list(filter(fun, emails))

# no of email ids
n = 3 
emails = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)