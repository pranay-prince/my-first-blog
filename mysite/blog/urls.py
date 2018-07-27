from django.conf.urls import url 
from . import views
urlpatterns=[
    url('post/new/$', views.post_new, name='post_new'),
	url(r'post/(?P<pk>[^/]+)/$', views.post_detail, name='post_detail'),
    url(r'post/(?P<pk>[^/]+)/edit/$', views.post_edit, name='post_edit'),
	url('$', views.post_list, name='post_list'),
]