from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^home/register$', views.register),
    url(r'^home/login$', views.validate_login),
    url(r'^home/success$', views.success),
    url(r'^home/wall$', views.wall),
    url(r'^home/logoff$', views.logoff),
    url(r'^home/post_message$', views.post_message),
    url(r'^home/post_comment$', views.post_comment),
]
