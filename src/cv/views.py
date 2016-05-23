from django.http import HttpResponse
from django.shortcuts import render

from io import BytesIO

from .cv import CvPdf, CVPdf


def test(request):
    template = 'cv/test_form.html'
    return render(request, template, {})

def test_generate(request):
    response = HttpResponse(content_type = 'application/pdf')
    response['Content-Dispotion'] = 'filename="test.pdf"'

    buffer = BytesIO()

    cv = CVPdf(buffer)
    #pdf = cv.report()
    cv.report()

    # cv = CvPdf(response)
    # # cv.test_drawing()
    # cv.tutorial()
    # cv.show()
    # cv.save()

    return response
