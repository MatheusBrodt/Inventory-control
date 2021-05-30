from reportlab.pdfgen import canvas
from datetime import datetime

day = datetime.today().day
month = str(datetime.today().month)
zero = '0'
if '10' in month or '11' in month or '12' in month:
    zero = ''
year = datetime.today().year
data = str(f'{day}/{zero}{month}/{year}')

pdf = canvas.Canvas('C:/Users/mathe/Documents/Relatorio de Montagem Laboratório.pdf')
pdf.setFont('Times-Bold', 25)
pdf.drawString(240, 810, f'{data}')
pdf.setFont('Times-Bold', 20)
pdf.drawString(155, 780, "Relatório de montagem CAROL")
pdf.save()
