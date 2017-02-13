from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^appetizer$', views.appetizer, name='appetizer'),
	url(r'^maincourse$', views.maincourse, name='maincourse'),
	url(r'^dessert$', views.dessert, name='dessert'),
	url(r'^post/(?P<pk>\d+)/hapus/$', views.hapus, name='hapus'),
]