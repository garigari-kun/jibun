from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cv_form/$', views.test, name = 'cv_form' ),
    url(r'^cv_generate/$', views.test_generate, name = 'cv_generate'),
]
