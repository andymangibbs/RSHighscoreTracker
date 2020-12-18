import xlrd


def excel_reader(keyword):
    # open excel sheet
    loc = "C:/Users/andym/PycharmProjects/RunescapeHSTracker/" + keyword + ".xlsx"
    final_list = []

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    rows_total = sheet.nrows
    col_total = 4
    start_row = 0
    start_col = 0

    for i in range(rows_total):
        for r in range(col_total):
            rows_val = sheet.row_values(i)
            if rows_val[r] == "Rank":
                start_col = r
                start_row = i+1

    # create a list of all of the cells in the sheet
    for row in range(start_row, rows_total):
        temp_list = []
        for column in range(start_col, col_total):
            temp_list.append(sheet.cell_value(row, column))
        final_list.append(temp_list)
    return final_list
