from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^home/register$', views.register),
    url(r'^home/login$', views.validate_login),
    url(r'^home/success$', views.success),
]
