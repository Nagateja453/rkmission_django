from django.conf.urls import url
from krish import views

urlpatterns = [
	url(r'^$', views.index2, name="index2"),
	url(r'^addpost/$', views.author1, name="author1"),
	url(r'^table/$', views.list, name="list"),
	url(r'^gallery/$',views.gallery, name="gallery"),
	url(r'^test/$',views.test, name="test"),
	url(r'^latest-news/$',views.latest_news, name="latest_news"),
	url(r'^test/$',views.test, name="test"),
	url(r'^addpage/$', views.addpage, name="addpage"),
	url(r'^about/(?P<slug>[-\w]+)/$',views.about, name='about'),
	url(r'^academics/(?P<slug>[-\w]+)/$',views.academics, name='academics'),
	url(r'^fees/(?P<slug>[-\w]+)/$',views.fees, name='fees'),
	url(r'^admissions/(?P<slug>[-\w]+)/$',views.admissions, name='admissions'),
	url(r'^careers/(?P<slug>[-\w]+)/$',views.careers, name='careers'),
	url(r'^infrastructure/(?P<slug>[-\w]+)/$',views.infrastructure, name='infrastructure'),
	url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
	url(r'^add_page_list/$', views.add_page_list, name="add_page_list"),
	url(r'^edit_add_page/(?P<id>\d+)/$', views.edit_add_page, name='edit_add_page'),
	url(r'^domestic_donations/$',views.domestic_donations, name="domestic_donations"),
	url(r'^domestic_donation_view/$',views.domestic_donation_view, name="domestic_donation_view"),
	url(r'^contactus/$', views.contactus, name="contactus"),
	url(r'^(?P<slug>[-\w]+)/$',views.sriram, name='sriram'),
	
]