import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 

data=pd.read_csv("apple_products.csv")
# print(data.head())  #yani is data ki start vali kuch rows dikhao

# print(data.isnull().sum())  #y check krna k data m null values hn ya nhi, agar hn to jitni
# bhi null values ek column m hn to un ko sum() kr k dedo yani is s pta lgy ga k ek
# column m kitni null values hn------  this is a step in data cleaning.  (vesy is ki
# output m hr column k agy zero h yani kisi column m koi null value nhi)

# print(data.describe())  #is s poory data k columns ka mean, std, min, max etc etc show hota


# 10 high rated phones k models check kro (yani 10 esy models jin ki star rating sab s 
# ziada h)
sorted_data=data.sort_values(['Star Rating'],ascending=False) #yani star rating valy column
# ki base pr sort kro (column ki base pr sort kia isi liye is vali [] m likha), or descending
# order m sort kro ta k phly 10 high rated show hon or hm un ko utha len

# highest_rated=sorted_data.head(10)  #yani is data ki phli 10 rows dikhao
# iphone=(highest_rated["Product Name"].value_counts()) 
# label=iphone.index 
# count=highest_rated["Number Of Ratings"]
# figure=px.bar(highest_rated, x=label, y=count, title="number of ratings of highest rated iphones")
# figure.show()   #yani poory data set m s vo phly 10 phones jo k high star rating valy hn, un phones ko raph ki
# form m is trah dikhao k x-axis pr phone ay or y-axis pr y btaya ja rha ho k kis phone ki sab s ziada number of
# ratings hn.

# ab hm y bhi dekh lety hn k kis phone k sab s ziada reviews pry hn, chahy vo reviews achy ho ya bury hun, 
# bas y chahye k reviews kitny hn

# highest_rated=sorted_data.head(10)
# label=(highest_rated["Product Name"].value_counts())
# iphones=label.index
# number_of_reviews=(highest_rated["Number Of Reviews"])
# figure=px.bar(highest_rated, x=iphones, y=number_of_reviews, title="number of reviews of highest rated iphones")
# figure.show()


# we can represent via scatter plot to show the relationship between number of ratings and sale price

# figure=px.scatter(data_frame=data, x="Number Of Ratings", y="Sale Price", size="Discount Percentage", 
#                   trendline="ols", title="relationship between number of ratings and discount percentage")
# figure.show()

# yhan y inverse relationship show kr rha yani, jesy jesy sale price brhati gay, vesy vesy ratings km hoti gi

# check kro k jesy jesy discount percantage ko brhaya to kia ratings brhi
figure=px.scatter(data_frame=data, x="Discount Percentage", y="Number Of Ratings", size="Sale Price", trendline="ols", 
                  title="relationship between number of rating and discount percentage")
figure.show()   #it shows direct relationship, yani jesy jesy hm n discount ko increase kia to hmari
# number of ratings brhi yani kha ja skta h k ziada logo n phone buy kia, but this is not always the case
