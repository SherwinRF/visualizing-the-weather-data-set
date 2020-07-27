# --------------
# Import the required Libraries
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import calendar
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Generate a line chart that visualizes the readings in the months

def line_chart(df,period,col):
    """ A line chart that visualizes the readings in the months
    
    This function accepts the dataframe df ,period(day/month/year) and col(feature), which plots the aggregated value of the feature based on the periods. Ensure the period labels are properly named.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    period - Period of time over which you want to aggregate the data
    col - Feature of the dataframe
    
    """
    mths = ['January', 'February', 'March', 'April','May','June', 'July', 'August','September', 'October', 'November', 'December']
    period = pd.to_datetime(period).strftime('%B')
    agg_val = df.groupby(period)[[col]].mean()
    agg_val = agg_val.reindex(mths)
    plt.plot(agg_val.index, agg_val)
    plt.xlabel('Months')
    plt.ylabel('Temp (C)')
    plt.title('Temperature Trend, 2012')
    plt.xticks(rotation = 90) 
    return
    

# Function to perform univariate analysis of categorical columns
def plot_categorical_columns(df):
    """ Univariate analysis of categorical columns
    
    This function accepts the dataframe df which analyzes all the variable in the data and performs the univariate analysis using bar plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    
    """
    cat = df.select_dtypes(include = 'object')
    plt.figure(figsize=(15,10))
    sns.countplot(x = 'Weather', data = cat)
    plt.xticks(rotation = 90)
    plt.show()
    return


# Function to plot continous plots
def plot_cont(df,plt_typ):
    """ Univariate analysis of Numerical columns
    
    This function accepts the dataframe df, plt_type(boxplot/distplot) which analyzes all the variable in the data and performs the univariate analysis using boxplot or distplot plot.
    
    Keyword arguments:
    df - Pandas dataframe which has the data.
    plt_type - type of plot through which you want to visualize the data
    
    """
    nc = df.select_dtypes(include = 'number')
    fig, ((ax_1, ax_2), (ax_3, ax_4), (ax_5, ax_6)) = plt.subplots(3,2, figsize=(15,10) )
    
    if plt_typ == 'boxplot':
        sns.boxplot(nc["Temp (C)"], ax = ax_1)
        sns.boxplot(nc["Dew Point Temp (C)"], ax = ax_2)
        sns.boxplot(nc["Rel Hum (%)"], ax = ax_3)
        sns.boxplot(nc["Wind Spd (km/h)"], ax = ax_4)
        sns.boxplot(nc["Visibility (km)"], ax = ax_5)
        sns.boxplot(nc["Stn Press (kPa)"], ax = ax_6)
    if plt_typ == 'distplot':
        sns.distplot(nc["Temp (C)"], ax = ax_1)
        sns.distplot(nc["Dew Point Temp (C)"], ax = ax_2)
        sns.distplot(nc["Rel Hum (%)"], ax = ax_3)
        sns.distplot(nc["Wind Spd (km/h)"], ax = ax_4)
        sns.distplot(nc["Visibility (km)"], ax = ax_5)
        sns.distplot(nc["Stn Press (kPa)"], ax = ax_6)
    return
    

# Function to plot grouped values based on the feature
def group_values(df,col1,agg1,col2):
    """ Agrregate values by grouping
    
    This function accepts a dataframe, 2 column(feature) and aggregated function(agg1) which groupby the dataframe based on the column and plots the bar plot.
   
    Keyword arguments:
    df - Pandas dataframe which has the data.
    col1 - Feature of the dataframe on which values will be aggregated.
    agg1 - Dictionary of aggregate functions with feature as the key and func as the value
    col2 - Feature of the dataframe to be plot against grouped data.
    
    Returns:
    grouping - Dataframe with all columns on which it is grouped on.
    """
    aggregate = {'mean':np.mean,'max':np.max,'min':np.min,'sum':np.sum,'len':len}
    grouping = df.groupby(col1)[[col2]].agg(aggregate[agg1])
    return grouping
    

# Read the Data and pass the parameter as parse_dates=True, index_col='Date/Time'
weather_df = pd.read_csv(path, parse_dates=True, index_col='Date/Time')

# Lets try to generate a line chart that visualizes the temperature readings in the months.
# Call the function line_chart() with the appropriate parameters.
line_chart(weather_df, weather_df.index, 'Temp (C)')

# Now let's perform the univariate analysis of categorical features.
# Call the "function plot_categorical_columns()" with appropriate parameters.
plot_categorical_columns(weather_df)

# Let's plot the Univariate analysis of Numerical columns.
# Call the function "plot_cont()" with the appropriate parameters to plot distplot
plot_cont(weather_df, 'distplot')

# Call the function "plot_cont()" with the appropriate parameters to plot boxplot
plot_cont(weather_df, 'boxplot')

# Groupby the data by Weather and plot the graph of the mean visibility during different weathers. Call the function group_values to plot the graph.
# Feel free to try on diffrent features and aggregated functions like max, min.
a = group_values(weather_df, 'Weather', 'mean', 'Visibility (km)')
a.plot( kind = 'bar', figsize=(15,10) )
plt.show()



