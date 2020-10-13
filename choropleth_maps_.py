#import plotly.plotly as pt
import chart_studio.plotly as pt
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs,plot,iplot,init_notebook_mode
init_notebook_mode(connected=True)

data1 = dict(type = 'choropleth' , locations = ['AZ','CA','NY','WA','WY'] , locationmode = 'USA-states' , 
# if we have codes for country then use 'USA-states', if u have state full name then use 'country names'
colorscale ='Greens' , text =['text1','text2','text3','text4','text5'] , z= [1,2,3,4,5], colorbar ={'title':'Colorbar Title'})
layout1 = dict(geo= {'scope':'usa'})
choromap = go.Figure(data=[data1],layout=layout1)
iplot(choromap)
# colorscale : Viridis, reversescale=True

ds = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/US_agri_map_data.csv')
print (ds.head(2))

data2 = dict(type='choropleth',locations = ds['code'],locationmode = 'USA-states' , colorscale ='Greens', 
text=ds['category'], z=ds['total exports'],
colorbar={'title':'Colorbar title'})
layout2 = dict(title = 'US Agriculture data ',geo= {'scope':'usa'})
choromap1 = go.Figure([data2],layout2)
iplot(choromap1)

ds2 = pd.read_csv('/Users/skarthi/Documents/Python_Scripts_Basics/Data/gdp.csv')
print (ds2.head(2))

wmap_ds = dict(type='choropleth',locations=ds2['CODE'],colorscale='Greens', text=ds2['COUNTRY'],z= ds2['GDP (BILLIONS)'],colorbar={'title':'GDP billions '})
layout3= dict(title='World GDP (Billions)',geo=dict(showframe=False,projection={'type':'stereographic'}))
choromap3 = go.Figure([wmap_ds],layout3)
iplot(choromap3)