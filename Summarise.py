import numpy as np
import pandas as pd

### Constructing the dataframe for summarising numerical data
def numeric_summary(imported_data, groups):
    numeric_sum = pd.DataFrame(['', '', 'count', 'unique entries', 'mean', 'std dev', 'median', '25th quartile', '75th quartile', 'min', 'max'])

    ### Temp dataframe containg only group 1. This is used to create a list of columns that contain numerical data
    temp_dataframe = pd.DataFrame(imported_data[0])
    numeric_cols = []
    for col in temp_dataframe.columns:
        if temp_dataframe[col].dtype == 'float64':
            numeric_cols.append(col)


    ### Iterate through list of numerical columns
    for j, i in enumerate(numeric_cols):
        group = 0
        while group < len(imported_data):

            ### Create a dataframe for group currently being iterated through (group i)
            df = pd.DataFrame(imported_data[group])

            ### Generate all the summary data for current group in the current column
            numeric_sum[i + ' - ' + str(group+1)] = [str(i),
                                                     'Group ' + str(group+1) + ' - ' + str(groups[group]),
                                                     df[i].count(),
                                                     df[i].nunique(),
                                                     round(df[i].mean(), 2),
                                                     round(df[i].std(), 2),
                                                     round(df[i].median(), 2),
                                                     round(df[i].quantile(q=0.25), 2),
                                                     round(df[i].quantile(q=0.75), 2),
                                                     df[i].min(),
                                                     df[i].max()]

            ### Add an empty column after all groups data summarised for current column
            if group + 1 == len(imported_data):
                numeric_sum[(j+1)*2+1] = ['','', '', '', '', '', '', '', '', '', '']

            group = group + 1

    return numeric_sum

### Constructing the dataframe for categorical value names, n, and %
def categorical_summary(df, groups):
    ### create a list that will contain columns names with categorical data
    categorical_names = list()

    ### Combine all the groups into a dataframe so the unique items and each column can be recorded
    combined_groups = pd.DataFrame()
    for i in range(len(df)):
        combined_groups = combined_groups.append(df[i])

    ### Create a list of all the unique entries in each column (excluding numerical data). Also creates list of column titles that contain categorial data (categorical_names)
    unique_items = ['', '']
    for col in combined_groups.columns:
        if combined_groups[col].dtype != 'float64':
            categorical_names.append(col)
            unique_item_current_col = combined_groups[col].unique()
            unique_items.append((col))
            for i in range(len(unique_item_current_col)):
                unique_items.append(unique_item_current_col[i])
            unique_items.append('')

    ### Add list of unique names to a dataframe that will summarise the data
    categorical_sum = pd.DataFrame(unique_items)

    ### Add n and % values to the summary dataframe
    ### Firstly iterates through groups
    for i in range(len(df)):
        categorical_n = list()
        categorical_p = list()
        col = 0

        ### Secondly iterates through rows for the current group
        for j in range(categorical_sum.shape[0]):
            current_val = categorical_sum.iloc[j][0]
            previous_val = 999

            ### Only define previous_val if the current row is not the first
            if j > 1:
                previous_val = categorical_sum.iloc[j-1][0]

            ### Keep the column blank if the corresponding variable column is blank (i.e. space between each header)
            if (current_val == '') & (j > 1):
                categorical_n.append('')
                categorical_p.append('')
                col = col + 1
            ### keep the current column blank if previous value was blank (allows for headers for each variable list)
            elif previous_val == '':
                categorical_n.append('')
                categorical_p.append('')
            ### adds group names to columns
            elif (j == 0) & (col == 0):
                categorical_n.append('Group ' + str(i+1) + ' - ' + str(groups[i]))
                categorical_p.append('Group ' + str(i+1)+  ' - ' + str(groups[i]))
            ### adds labels to columns
            elif (j == 1) & (col == 0):
                categorical_n.append('n')
                categorical_p.append('%')
            ### Otherwise, determine the count and %
            else:
                current_df = pd.DataFrame(df[i])
                current_count = len(current_df[current_df[categorical_names[col]] == current_val])
                categorical_n.append(current_count)
                categorical_p.append(str(round(current_count / len(current_df.index) * 100, 2)) + '%')

        ### Convert the lists to columns of the summary dataframe
        categorical_sum['group ' + str(i+1) + ' - n'] = categorical_n
        categorical_sum['group ' + str(i+1) + ' - %'] = categorical_p
    print(categorical_sum)

    return categorical_sum
