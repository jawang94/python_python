from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^home/create$', views.create),
    url(r'^home/login$', views.login),
    url(r'^home/success$', views.success),
]
