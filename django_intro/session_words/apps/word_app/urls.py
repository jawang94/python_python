from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^session_words$', views.index),
    url(r'^submit$', views.process),
    url(r'^clear$', views.clear),
]