from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users$', views.index),
    url(r'^users/create$', views.create),
    url(r'^process$', views.process),
    url(r'^show$', views.show),
    url(r'^destroy$', views.destroy),
    url(r'^edit$', views.edit),
    url(r'^process_edit$', views.process_edit)
]