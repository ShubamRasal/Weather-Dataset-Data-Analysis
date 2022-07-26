# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 14:12:21 2021

@author: Shubham
"""

import pandas as pd

import numpy as np

import os

os.chdir(r"D:\Data Analyst\ProjectPortfolio")
os.listdir()

Weather = pd.read_csv("Weather Data.csv")
Weather

# How to Analyze DataFrames ?

Weather.head()

Weather.shape

Weather.index

Weather.columns

Weather.dtypes

Weather["Weather Condition"].unique()

Weather.nunique()

Weather.count()

Weather['Weather Condition'].value_counts()

Weather.info()

# Lets find all the unique 'Wind Speed' values in the data.

Weather.head(5)

Weather.nunique()

Weather['Wind Speed_km/h'].nunique()

Weather['Wind Speed_km/h'].unique()

# Lets find the number of times when the 'Weather is exactly clear'.

Weather.head(2)

Weather.Weather.value_counts()

#filtering:
    
Weather.head(2)
Weather[Weather.Weather == 'Clear']

#Groupby()
Weather.groupby('Weather').get_group('Clear')

# Lets find the number of times when the "Wind Speed was exactly 4 km/h".
Weather.head(2)

Weather[Weather["Wind Speed_km/h"]==4]

#Lets find out all the null values in the data:
    
Weather.isnull().sum()

Weather.notnull().sum()
#therefore there is no null value

#Rename the column name "weather" of the dataframe to "Weather condition":
    
Weather.head(2)

Weather.rename(columns = {"Weather" : "Weather Condition"})

Weather.head(2)
# It has not gone permanently we have to use inplace=True:

Weather.rename(columns = {"Weather" : "Weather Condition"}, inplace=True)  


Weather.head(2)

# Let's find the mean "Visibility":

Weather.Visibility_km.mean()   

# Let's find the Standard Deviation of 'Pressure' in this data:

Weather.Press_kPa.std()

#Let's find the variance of 'Relative Humidity' in this  data:
    
Weather['Rel Hum_%'].var()

# Let's find all the instances when 'Snow' was recorded:
    
#value_count()

#Weather.head(2)

Weather['Weather Condition'].value_counts()

#Filtering:
    
Weather[Weather['Weather Condition'] == 'Snow']

#str.contains

Weather[Weather['Weather Condition'].str.contains('Snow')].tail(5)

# Let's find all instances when 'Wind Speed is above 24' and 'Visibility is 25':

Weather.head(2)

Weather[(Weather['Wind Speed_km/h']>24) & (Weather['Visibility_km']==25)]

#What is the Mean value of each column against each 'Weather Condition' :

Weather.head(2)

Weather.groupby('Weather Condition').mean()

#What is the minimum & maximum value of each column against each 'Weather Condition':
    
Weather.groupby('Weather Condition').min()
Weather.groupby('Weather Condition').max()

# Show all the Records where weather condition is Fog.

Weather[Weather['Weather Condition'] == 'Fog']

# Find all instances when 'Weather is Clear' or 'Visibility is above 40

Weather[(Weather['Weather Condition'] == 'Clear') | (Weather['Visibility_km']>40)]

# Find all instance When:
    
# a. 'Weather is Clear' and 'Relative Humidity is greater than 50'

or

# B. 'Visibility is above 40'

Weather.head(2)

Weather[(Weather['Weather Condition'] == 'Clear') & (Weather['Rel Hum_%']>50) | (Weather['Visibility_km']>40)]
