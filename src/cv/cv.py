from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

import datetime

class CvPdf(object):

    def __init__(self, response):
        self.pdf = canvas.Canvas(response)
        pdfmetrics.registerFont(UnicodeCIDFont('HeiseiMin-W3'))
        width, height = A4
        print('width: {}'.format(width))
        print('height: {}'.format(height))

    def test_drawing(self):
        self.pdf.drawString(100, 100, 'Hello, World')

    def tutorial(self):
        today = datetime.datetime.now()
        self.pdf.setLineWidth(.3)
        self.pdf.setFont('HeiseiMin-W3', 12)
        self.pdf.drawString(30, 750, 'Jibun')
        self.pdf.drawString(500, 750, '{}'.format(today.strftime('%Y / %m / %d')))
        self.pdf.line(480, 747, 580, 747)
        self.pdf.drawString(275, 725, '未払金')
        self.pdf.drawString(500, 725, '¥100,000')
        self.pdf.line(378,723,580,723)
        self.pdf.drawString(30,703,'RECEIVED BY:')
        self.pdf.line(120,700,580,700)
        self.pdf.drawString(120,703,"JOHN DOE")



    def show(self):
        self.pdf.showPage()

    def save(self):
        self.pdf.save()
