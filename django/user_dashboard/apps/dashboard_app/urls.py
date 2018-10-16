from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/dashboard$', views.dashboard),
    url(r'^destroy$', views.destroy),
    url(r'^edit$', views.edit),
    url(r'^process_edit$', views.process_edit),
    url(r'^home/register$', views.register),
    url(r'^home/validate_register$', views.validate_register),
    url(r'^home/add_new$', views.add_new),
    url(r'^home/validate_add_new$', views.validate_add_new),
    url(r'^home/login$', views.login),
    url(r'^home/validate_login$', views.validate_login),
    url(r'^home/success$', views.success),
    url(r'^home/wall$', views.wall),
    url(r'^home/logoff$', views.logoff),
    url(r'^home/post_message$', views.post_message),
    url(r'^home/post_comment$', views.post_comment),
]
