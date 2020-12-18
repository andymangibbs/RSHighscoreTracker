import xlsxwriter
import datetime
import skills


def excel_writer(keyword, skills_list):
    # create and excel sheet
    file_name = keyword + ".xlsx"

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet("Ree")

    bold = workbook.add_format({'bold': True})
    date = "Date: " + (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    worksheet.write('A1', 'Account Name-' + keyword, bold)
    worksheet.write('A2', date, bold)
    worksheet.write('B2', "Rank", bold)
    worksheet.write('C2', "Level", bold)
    worksheet.write('D2', "XP", bold)
    row = 2
    col = 0

    # populates cells in sheet with products
    cur = 0
    init_skills = skills.skills()

    for skill_cur in skills_list:
        worksheet.write(row, col, init_skills[cur])
        worksheet.write(row, col+1, skill_cur[0])
        worksheet.write(row, col+2, skill_cur[1])
        worksheet.write(row, col+3, skill_cur[2])
        cur += 1
        row += 1

    workbook.close()
