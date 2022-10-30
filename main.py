from pdf2docx import Converter
pdf_file = 'Automatisation_company_Python.pdf'
docx_file = 'Automatisation_company_Python1.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
