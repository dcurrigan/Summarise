##### ----- -   - ----- ----- -     ####
##### -      - -  -     -     -     ####
##### -----   -   -     ----- -     ####
##### -      - -  -     -     -     ####
##### ----- -   - ----- ----- ----- ####

#write to excel
import pandas as pd
import xlsxwriter

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('test1.xlsx', engine='xlsxwriter')

def write(data):
    # Convert the dataframe to an XlsxWriter Excel object.
    data.to_excel(writer, sheet_name='Sheet1', index=False, header=False)

    # Get the xlsxwriter objects from the dataframe writer object.
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    #create formatting options
    variable_format = workbook.add_format({'align': 'left', 'valign': 'vcenter', 'bold': True})
    general_format = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
    col_format = workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True})

    #Autosize column widths
    for col in data.columns:
        max_length = 0
        ### determine length of largest item in current column
        for row in data[col]:
            if len(str(row)) > max_length:
                max_length = len(str(row))

        ### get index number of current column and set its width to the max item width in that columns
        col_index = data.columns.get_loc(col)
        worksheet.set_column(col_index, col_index, max_length + 2, general_format)

        ### Set formatting for the first column (containing row names)
        if col_index == 0:
            worksheet.set_column(col_index, col_index, max_length + 2, variable_format)

    ### Set the formatting for the first row (containing column names)
    worksheet.set_row(0, 15, col_format)

    writer.save()
