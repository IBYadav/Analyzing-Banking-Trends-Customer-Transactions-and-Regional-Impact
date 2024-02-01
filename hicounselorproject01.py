# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 16:51:14 2024

@author: User
"""

#--- Import Pandas ---
import pandas as pd
#--- Read in dataset (user_nodes.csv) ----
file_path = './user_nodes.csv'
df = pd.read_csv(file_path)
#--- Inspect data ---
df
# --- WRITE YOUR CODE FOR TASK 2 ---
missing_values = df.isnull()
null_values = missing_values.sum()
#--- Inspect data ---
null_values
# --- WRITE YOUR CODE FOR TASK 3 ---
#duplicates =
duplicated_values = df.duplicated()
duplicates = duplicated_values.sum()
#--- Inspect data ---
duplicates
# --- WRITE YOUR CODE FOR TASK 4 ---
df.drop_duplicates(inplace=True) #dropping duplicates
#--- Inspect data ---
df
# --- WRITE YOUR CODE FOR TASK 5 ---
# Define the list of columns to remove
columns_to_remove = ["has_loan", "is_act"]

# Use the .drop() method to remove the specified columns
df.drop(columns=columns_to_remove, axis=1, inplace=True)

# Define a dictionary to rename columns
new_columns = {"has_loan":"new_column_1","is_act":"new_column_2","id_":"consumer_id","area_id_":"region_id","node_id_":"node_id","act_date":"start_date","deact_date":"end_date"}

# Use the .rename() method to rename the specified columns
df.rename(columns=new_columns, inplace=True)

# Export the modified DataFrame to a CSV file
df.to_csv('user_nodes_cleaned.csv',index=False)

# Inspect the data
df.columns
#--- Import Pandas ---
import pandas as pd
#--- Read in dataset----
file_path = './user_transactions.csv'
df1 = pd.read_csv(file_path)
#--- Inspect data ---
df1
# --- WRITE YOUR CODE FOR TASK 7 ---
missing_values = df1.isnull()
null_value = missing_values.sum()
#--- Inspect data ---
null_value
# --- WRITE YOUR CODE FOR TASK 8 ---
duplicate_values = df1.duplicated()
duplicate = duplicate_values.sum()
#--- Inspect data ---
duplicate
# --- WRITE YOUR CODE FOR TASK 9 ---
df1.drop_duplicates(inplace=True)
#--- Inspect data ---
df1
# --- WRITE YOUR CODE FOR TASK 10 ---
#--- Export the df1 as "user_transactions_cleaned.csv" ---
columns_to_remove= ["has_credit_card", "account_type"]
df1.drop(columns=columns_to_remove, axis=1, inplace=True)
new_columns = {
    'id_': 'consumer_id',
    't_date': 'transaction_date',
    't_type': 'transaction_type',
    't_amt': 'transaction_amount'
}
df1.rename(columns=new_columns, inplace=True)
df1.to_csv('user_nodes_cleaned.csv',index=False)
#--- Inspect data ---
df1