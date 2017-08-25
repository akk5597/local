import openpyxl as opx
from student.models import Book

wb = opx.load_workbook('F:\\GitHub\\local\\local\\locallibrary\\student\\media\\filefinal.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
logger = open('log.txt','w')

for row in range(2,1500):
	if sheet['A'+str(row)].value != None:
		logger.write(str(row)+': '+str(sheet['A'+str(row)].value))
		book = Book(
			id = sheet['A'+str(row)].value,
			title = sheet['B'+str(row)].value,
			author = sheet['C'+str(row)].value,
			publisher = sheet['D'+str(row)].value
		)
		book.save()