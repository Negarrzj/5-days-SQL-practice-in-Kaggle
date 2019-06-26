# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# import our bq_helper package (from Kaggle)
import bq_helper 
# create a helper object for our bigquery dataset (helper project from Kaggle)
open_aq = bq_helper.BigQueryHelper(active_project= "bigquery-public-data", 
                                       dataset_name = "openaq")

# print all the tables in this dataset 
open_aq.list_tables()

#writing a query to show all columns and rows
main_query = """ SELECT *
                FROM `bigquery-public-data.openaq.global_air_quality` """

# save the file in the form of CSV                
all_columns = open_aq.query_to_pandas_safe(main_query)

#show all columns
all_columns.columns

# print the few rows of the table called: global_air_quality
open_aq.head('global_air_quality')

##------------------------------------------------------------------------##
# question:  writing a query to show all "city" that their "country" is US
query= """ SELECT city
            FROM `bigquery-public-data.openaq.global_air_quality`
            WHERE country='US'"""

# the query_to_pandas_safe will only return a result if it's less
# than one gigabyte (by default)
us_cities = open_aq.query_to_pandas_safe(query)
##------------------------------------------------------------------------##
#question: What five cities have the most measurements taken there?
us_cities.city.value_counts().head()

#question: countries use a unit other than ppm to measure any type of pollution
unit_query = """SELECT distinct country, unit 
            FROM `bigquery-public-data.openaq.global_air_quality`
            WHERE unit != 'ppm' """
#convert result to csv file
country_unit = open_aq.query_to_pandas_safe(unit_query) 

#show result with two column unit and country
country_unit[['unit', 'country']]
##------------------------------------------------------------------------##
#question:Which pollutants have a value of exactly 0?
pollution_query = """SELECT distinct pollutant, value, country   
            FROM `bigquery-public-data.openaq.global_air_quality`
            WHERE value = 0 """
#query to pandas default less than 1G
pollution = open_aq.query_to_pandas_safe(pollution_query)

#few columns with desired result 
pollution[['country','pollutant','value']].head()
##------------------------------------------------------------------------##

