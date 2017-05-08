from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^edit/(?P<blog_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
    url(r'^blogContent/(?P<blog_id>[0-9]+)$', views.blog_page, name='blog_page'),
]
