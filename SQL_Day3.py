# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# library for plotting
import matplotlib.pyplot as plt

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.
# Your code goes here :)
# import package with helper functions 
import bq_helper

# create a helper object for this dataset
accidents = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                   dataset_name="nhtsa_traffic_fatalities")
#get all tables in this dataset
accidents.list_tables()
# heg 5 rows of 'accident_2015' tale
accidents.head('accident_2015')

#query to find which day of the week the most fatal traffic accidents happen on.
accidental_day_of_week_query = """SELECT COUNT(consecutive_number) as count_id, EXTRACT (DAYOFWEEK FROM timestamp_of_crash) as day_week
                                    FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
                                    
                                    GROUP BY day_week
                                    ORDER BY count_id DESC"""

#quwry to pandas
accidental_day_of_week = accidents.query_to_pandas_safe(accidental_day_of_week_query)
# see table result
accidental_day_of_week[['count_id','day_week']]
# or see result
print(accidental_day_of_week)

# make a plot to show that our data is, actually, sorted:
plt.plot(accidental_day_of_week.count_id)
plt.title("Number of Accidents by Rank of Day \n (Most to least dangerous)")
#_________________________________________________________________________________________
#  question: Which hours of the day do the most accidents occur during?

# query to find hours of the day do the most accidents accur during
accidental_our_day_query = """ SELECT COUNT(consecutive_number) as countID ,EXTRACT (HOUR FROM timestamp_of_crash) as hour_day
                         FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015`
                         GROUP BY hour_day
                         ORDER BY countID DESC"""

# convert query to pandas table 
accidental_our_day = accidents.query_to_pandas_safe(accidental_our_day_query)

#print result
print(accidental_our_day)

# more practice for myself
plt.plot(accidental_our_day.countID)
#___________________________________________________________________________________________
#Question: Which state has the most hit and runs?
# query to find which state has the most hit and runs
hit_and_run_state_query = """ SELECT COUNT(hit_and_run) as count_hit_run, registration_state_name
                              FROM `bigquery-public-data.nhtsa_traffic_fatalities.vehicle_2015`                        
                              GROUP by registration_state_name
                              ORDER by count_hit_run DESC"""

# query to pandas 
hit_and_run_state = accidents.query_to_pandas_safe(hit_and_run_state_query)

# see result
print(hit_and_run_state)