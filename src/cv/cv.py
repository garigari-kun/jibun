from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.units import cm



class CvPdf(object):

    def __init__(self, response):
        self.pdf = canvas.Canvas(response)

    def test_drawing(self):
        self.pdf.drawString(100, 100, 'Hello, World')

    def show(self):
        self.pdf.showPage()

    def save(self):
        self.pdf.save()
