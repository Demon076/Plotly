import plotly.express as px
import pandas as pd
df = pd.read_csv('trees.csv')
fig = px.imshow(df)
fig.show()

m=pd.read_csv('oscar_age_male.csv')
f=pd.read_csv('oscar_age_female.csv')

lst=[]
for i in range(len(f)):
    lst.append('F')
f['Gender']=lst

lst1=[]
for i in range(len(m)):
    lst1.append('M')
m['Gender']=lst1


df=pd.concat([m,f])
fig=px.scatter_3d(df,x='Gender',y='Year',z='Age')
fig.show()