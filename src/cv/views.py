from django.http import HttpResponse
from django.shortcuts import render

# from reportlab.pdfgen import canvas

from .cv import CvPdf


def test(request):
    template = 'cv/test_form.html'
    return render(request, template, {})

def test_generate(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Dispotion'] = 'filename="test.pdf"'

    # pdf = canvas.Canvas(response)
    # pdf.drawString(100, 100, 'Hello, World')
    #
    # pdf.showPage()
    # pdf.save()

    cv = CvPdf(response)
    # cv.test_drawing()
    cv.tutorial()
    cv.show()
    cv.save()

    return response
