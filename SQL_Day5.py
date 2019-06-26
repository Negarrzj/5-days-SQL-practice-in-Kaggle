# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory

import os
print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.

# query to find how many commits (recorded in the "sample_commits" table) have been made in repos written in the Python programming language?
python_commit_query = ("""
                        WITH python_repos AS (
                            SELECT DISTINCT repo_name -- Notice DISTINCT
                            FROM `bigquery-public-data.github_repos.sample_files`
                            WHERE path LIKE '%.py')
                        SELECT commits.repo_name, COUNT(commit) AS num_commits
                        FROM `bigquery-public-data.github_repos.sample_commits` AS commits
                        JOIN python_repos
                        ON  python_repos.repo_name = commits.repo_name
                        GROUP BY commits.repo_name
                        ORDER BY num_commits DESC
                                """)

# query to pandas 
python_commit = github.query_to_pandas_safe(python_commit_query, max_gb_scanned=6)

# print result
print(python_commit)

# plot result
import matplotlib.pyplot as plt   # import library 
plt.barh(python_commit.repo_name,python_commit.num_commits,log=True)