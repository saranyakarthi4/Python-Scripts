#import plotly.plotly as pt
import chart_studio.plotly as pt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs,plot,iplot,init_notebook_mode
init_notebook_mode(connected=True)

# 1 World Choropleth
ds = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/world_power.csv')
print (ds.head(2))

wmap_ds = dict(type='choropleth',locations=ds['Country'],colorscale='Greens', text=ds['Text'],z= ds['Power Consumption KWH'],colorbar={'title':'Power Consumptions KWH '},locationmode ='country names')
layout3= dict(title='World Power Consumptions',geo=dict(showframe=False,projection={'type':'natural earth'}))
choromap3 = go.Figure([wmap_ds],layout3)
iplot(choromap3)

# 2 US Choropleth
ds1 = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/election_data.csv')
print (ds1.head(2))
data1 = dict(type='choropleth',locations=ds1['State Abv'],text=ds1['State'], 
z= ds1['Voting-Age Population (VAP)'],colorbar={'title':'US Election 2012'},colorscale='Greens',locationmode ='USA-states')
layout= dict(title='US Election 2012',geo= {'scope':'usa'})
choromap4 = go.Figure([data1],layout)
iplot(choromap4)

