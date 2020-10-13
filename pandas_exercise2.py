import numpy as np
import pandas as pd

ecom = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/ecom_data.csv')

print (ecom.head(1))
print (ecom.info())  # len(ecom.columns)

# Avg purchase price
print (ecom['Purchase Price'].mean())

# Min/Max Purchase price
print (ecom['Purchase Price'].min())
print (ecom['Purchase Price'].max())

#How many people have English 'en' as languauge choice on the webite
print (ecom[ecom['Language']=='en'].count())

#How many people have job title as 'Lawyer'
print (ecom[ecom['Job']=='Lawyer'].count())

#how many people made purcahse during AM and PM
print (ecom.groupby('AM or PM').count()) 
print (ecom['AM or PM'].value_counts())


# top 5 common titles
print (ecom['Job'].value_counts().head(5))

# someone purchased from LOT: 90 WT what is the purchase price for the transaction
print ('someone purchased from LOT: 90 WT what is the purchase price for the transaction')
print (sum(ecom[ecom['Lot']== '90 WT']['Purchase Price']))


print ('Email of the person with credit card ')
print (ecom[ecom['Credit Card'] == 6011929061123406]['Email'])

print ('People having American express and made purchase over $95')
print (ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count() ) 

print ('How many people have credit card that expires in 2025')
print (ecom[ecom['CC Exp Date'].apply(lambda x: x[3:]=='25')].count())

print ('what are the top 5 most popular eamil providers')
ecom['Email Provider'] =  ecom['Email'].apply(lambda x: x.split('@')[1])
print (ecom['Email Provider'].value_counts().head(5))