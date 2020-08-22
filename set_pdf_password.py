# pip install PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader

file=input("enter the file name: ")

pdf_writer= PdfFileWriter()

pdf_file= PdfFileReader(file) # for read my pdf file

for page_num in range(pdf_file.numPages):
	pdf_writer.addPage(pdf_file.getPage(page_num))

set_password=input("Please Set the Password: ")

pdf_writer.encrypt(set_password)

with open(file, 'wb') as f:
	pdf_writer.write(f)
	f.close()

input()	