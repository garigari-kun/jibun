from django.http import HttpResponse
from django.shortcuts import render

from reportlab.pdfgen import canvas


def test(request):
    template = 'cv/test_form.html'
    return render(request, template, {})

def test_generate(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Dispotion'] = 'filename="test.pdf"'

    pdf = canvas.Canvas(response)
    pdf.drawString(100, 100, 'Hello, World')

    pdf.showPage()
    pdf.save()

    return response
