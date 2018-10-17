from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.index),
    url(r'^home/to_dashboard$', views.to_dashboard),
    url(r'^home/dashboard$', views.dashboard),
    url(r'^home/destroy$', views.destroy),
    url(r'^home/edit$', views.edit),
    url(r'^home/process_edit$', views.process_edit),
    url(r'^home/process_edit_password$', views.process_edit_password),
    url(r'^home/register$', views.register),
    url(r'^home/validate_register$', views.validate_register),
    url(r'^home/add_new$', views.add_new),
    url(r'^home/validate_add_new$', views.validate_add_new),
    url(r'^home/login$', views.login),
    url(r'^home/validate_login$', views.validate_login),
    url(r'^home/success$', views.success),
    url(r'^home/add_success$', views.add_success),
    url(r'^home/session_handler$', views.session_handler),
    url(r'^home/wall$', views.wall),
    url(r'^home/logoff$', views.logoff),
    url(r'^home/post_message$', views.post_message),
    url(r'^home/post_comment$', views.post_comment),
]
