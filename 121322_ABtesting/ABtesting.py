import pandas as pd 
import datetime
from datetime import date, timedelta
import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
pio.templates.default = "plotly_white"

# Read the data files
control_data = pd.read_csv("control_group.csv", sep = ";")
test_data = pd.read_csv("test_group.csv", sep = ";")

# Check the headings of the data
print(control_data.head())
print(test_data.head())


## Data Preparation ##

control_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions", "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Purchases"]
test_data.columns = ["Campaign Name", "Date", "Amount Spent", "Number of Impressions", "Reach", "Website Clicks", "Searches Received", "Content Viewed", "Added to Cart", "Purchases"]

print(control_data.isnull().sum())
print(test_data.isnull().sum())
# Q: The column "Reach" not appeared in the list, even if the number of columns and the list of the columns are the same
# print(control_data["Reach"].isnull().sum())

# 'inplace' indicates to make changes in the original data frame itself if True
# () should be followed by 'mean' function
control_data["Number of Impressions"].fillna(value = control_data["Number of Impressions"].mean(), inplace = True)
control_data["Reach"].fillna(value = control_data["Reach"].mean(), inplace = True)
control_data["Website Clicks"].fillna(value = control_data["Website Clicks"].mean(), inplace = True)
control_data["Searches Received"].fillna(value = control_data["Searches Received"].mean(), inplace = True)
control_data["Content Viewed"].fillna(value = control_data["Content Viewed"].mean(), inplace = True)
control_data["Added to Cart"].fillna(value = control_data["Added to Cart"].mean(), inplace = True)
control_data["Purchases"].fillna(value = control_data["Purchases"].mean(), inplace = True)

# Create a new data by merging both control and test data
# ()(outer) and [](inner) are needed for the 'sort_values'
# how = "outer" means to use unition of keys from both frames; returns a join over the union of the input columns
# how = "inner" means to use intersection of keys from both frames; contains the intersection of the two sets of inputs
ab_data = control_data.merge(test_data, how = "outer").sort_values(["Date"])
# drop = False means to add the replaced index column to the data; the current index will be deleted entirely and the numeric index will replace it
# drop = True means to delete the index
ab_data = ab_data.reset_index(drop = True)
print(ab_data.head())

# Check whether both data have the same sample size
print(ab_data["Campaign Name"].value_counts())


## A/B Testing to Find the Best Marketing Strategy ##

# The relationship between the number of impressions and the amount spent on both campaigns
# Create a scatter plot (figure)
figure = px.scatter(data_frame = ab_data, x = "Number of Impressions", y = "Amount Spent", size = "Amount Spent", color = "Campaign Name", trendline = "ols")
figure.show()

# The number of searches performed on the website from both campaigns
# Set up variables
label = ["Total Searches from Control Campaign", "Total Searches from Test Campaign"]
counts = [sum(control_data["Searches Received"]), sum(test_data["Searches Received"])]
colors = ['gold', 'lightgreen']
# Create a pie chart (figure)
fig = go.Figure(data = [go.Pie(labels = label, values = counts)])
fig.update_layout(title_text = "Control vs. Test: Searches")
fig.update_traces(hoverinfo = "label+percent", textinfo = "value", textfont_size = 30, marker = dict(colors = colors, line = dict(color = 'black', width = 3)))
fig.show()