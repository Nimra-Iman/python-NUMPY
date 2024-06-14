# screen time analysis is the task of analyzing and creating a report on which
# applications and websites are used by how much time.apple devices have one
# of the best ways of creating a screen time report

# on average, ek person kisi website ko kitna visit krta h
import numpy as np
import pandas as pd
import plotly.express as px
data=pd.read_csv("Screentime - App Details.csv")
# print(data.isnull().sum())
print(data.describe())
time_Spend=data["Times opened"]
app=data["App"]

# kis date ko sab s ziada screen use hui
date=data["Date"]
usage=data["Usage"]
# figure=px.bar(data, x=date, y=usage, color="App",title="kis date ko sab s ziada use hua")
# figure=px.bar(data_frame=data, x="Times opened", y="Notifications", color="App",title="relation between notifications and times opened")
figure=px.scatter(data_frame=data, x="Times opened", y="Notifications", color="App",trendline="ols",
                  title="relation between notifications and times opened")  #y bta rha h k 
                            # jitny notifications ziada hin gy, utni ziada dfa open ho gi app 
figure.show()



