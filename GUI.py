import numpy as np
import pandas as pd
import Summarise
import xl_writer


# Import data and remove accessory NaN rows imported with CSV file (NOTE This eliminates any row with 'NaN' in first column)
file_name = 'Data1.CSV'
df = pd.read_csv(file_name)
df = df[pd.notnull(df.iloc[:, 0])]

# Start-up text
print('Data Summary V1.0 - by Dale Currigan')
print('Exploratory data analysis made simple')
print('')
print('Currently loaded data file is: ' + file_name)
print('')
print('Hit Enter to continue')
input()

# Define groups
x = 0
col = ''
while x == 0:
    print("Which column contains the groups? (x to see column list, case sensitive)")
    col = input()
    if col == 'x':
        print(df.columns)
    else:
        x = 1

# Creates a list of each unique item (i.e. group) present in the column
groups = df[col].unique()
# Gets relative count of each group and stores in a dictionary
groups_summary = {}
for i in range (len(groups)):
    groups_summary[groups[i]] = len(df[df[col] == groups[i]])

print('')
print('There are ' + str(len(groups)) + ' groups in this column')
print('The groups and their relative counts are: ')
print(groups_summary)
print('')

# Create a list (named 'data') with each groups data as a separately indexed items
data = []
for i in range(len(groups)):
    data.append(df[df[col] == groups[i]])

# Options page
x = 0
while x == 0:
    print('What would you like to do?')
    print('1. Summarise numerical data')
    print('2. Summarise categorical data')
    print('')
    response = input()

    if response == '1':
        xl_writer.write(Summarise.numeric_summary(data, groups))
        x = 1
    elif response == '2':
        xl_writer.write(Summarise.categorical_summary(data, groups))
        x = 1
    else:
        print('Invalid entry. Try again')
        print('')





