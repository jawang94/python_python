from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^courses$', views.index),
    url(r'^process$', views.process),
    url(r'^delete$', views.delete),
    url(r'^destroy$', views.destroy),
]
