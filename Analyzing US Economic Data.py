# Importing libraries.
import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

# Define the function makeDashboard.
def makeDashboard(x, gdpChange, unemployment, title, fileName):
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdpChange.squeeze(), color="firebrick", line_width=4, legend_label="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend_label="% unemployed")
    show(p)

# The dictionay links contain the CSV files with all the data. 
# GDP is the file contains the GDP data. 
# Unemployment contains the unemployment data.
links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

# Pandas dataframes that contains the GDP data.
gdpData = pd.read_csv(links['GDP'])

# Displaying first five rows of the GDP data.
gdpData.head()

# Pandas dataframes that contains the unemployment data.
unemploymentData = pd.read_csv(links['unemployment'])

# Displaying first five rows of the GDP data.
unemploymentData.head()

# Displaying a dataframe where unemployment was greater than 8.5%.

unemploymentAbove = unemploymentData[unemploymentData["unemployment"] > 8.5]
unemploymentAbove

# Calling the function to produce a dashboard.
x = pd.DataFrame(data=gdpData, columns=['date'])

# New dataframe with the column 'change-current' called gdpChange from the dataframe that contains the GDP data.
gdpChange = pd.DataFrame(data=gdpData, columns=['change-current'])

# New dataframe with the column 'unemployment' called unemployment from the dataframe that contains the unemployment data.
unemployment = pd.DataFrame(data=unemploymentData, columns=['unemployment'])

#Assign it to the variable title.
title = 'GDP and Unemployment Stats'

# The name of the file is "index.html" and it will be stored in the varable file_name.
fileName = "index.html"

#Calling the function to produce a dashboard.
makeDashboard(x=x, gdpChange=gdpChange, unemployment=unemployment, title=title, fileName=fileName)