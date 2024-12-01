import xlsxwriter
from pars_club import array

def writer(parametr):

    book = xlsxwriter.Workbook(r"C:\GITHUB\Parsing\scraping_club.xlsx")
    sheet = book.add_worksheet("Товари")

    row = 0
    column = 0

    sheet.set_column("A:A", 20)
    sheet.set_column("B:B", 20)
    sheet.set_column("C:C", 50)
    sheet.set_column("D:D", 50)

    for item in parametr():
        sheet.write(row, column, item[0])
        sheet.write(row, column + 1, item[1])
        sheet.write(row, column + 2, item[2])
        sheet.write(row, column + 3, item[3])
        row += 1

    book.close()

if array != None:
    writer(array)


