from pdf2docx import Converter
pdf_file = 'Models_AI_on_Python.pdf'
docx_file = 'Models_AI_on_Python.docx'
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
