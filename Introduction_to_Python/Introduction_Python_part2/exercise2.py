# Data science for life science
# Introduction to Python

from numpy.core.fromnumeric import std
import pandas as pd
import numpy as np

# Exercise 2 - Introduction to Pandas
print("Exercise2 - Introduction to Pandas")

# Reading a csv file with Pandas
my_df = pd.read_csv("example_csv.csv", index_col = 0)

# Data exploration
print("\nDF head:\n", my_df.head(5))
print("\nDF tail:\n", my_df.tail(5))

# Check structure
print("\nDF structure:", my_df.shape)

# Get the transpose of this matrix for further analysis
my_df_T = my_df.transpose()

# Get the statistics of the dataframe
my_df_stats = my_df.describe()

# Locate the standard deviation for Wed
std_wed = my_df_stats.loc["std", "Mon"]
print("std_wed = ", std_wed)

# Indexing dataframes

# Dropping and adding information

# Outputting files
