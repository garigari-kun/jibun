from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    template = 'cv/test_form.html'
    return render(request, template, {})
