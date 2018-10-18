from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dashboard$', views.dashboard),
    url(r'^validate_register$', views.validate_register),
    url(r'^validate_login$', views.validate_login),
    url(r'^logoff$', views.logoff),
    url(r'^success$', views.success),
    # url(r'^destroy$', views.destroy),
    url(r'^add_book$', views.add_book),
    url(r'^validate_add_book$', views.validate_add_book),
    url(r'^add_success$', views.add_success),
    # url(r'^session_handler$', views.session_handler),
    url(r'^book$', views.book),
    url(r'^post_review$', views.post_review),
    url(r'^user$', views.user),
]
