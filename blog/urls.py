from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^edit/(?P<blog_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
    url(r'^blogContent/(?P<blog_id>[0-9]+)$', views.get_details, name='get_details'),
    url(r'^about/$',views.aboutMe,name='aboutMe'),
]
