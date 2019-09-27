# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from krish.models import AddPost, Imageshow,Testinomials,Latestnews,AddPage,Donations
from django.http import HttpResponse, HttpResponseRedirect
from krish.forms import AddPostForm, ImageForm,TestForm,latnewsForm,AddpageForm,DonationsForm
from django.shortcuts import get_object_or_404

#Create your views here.
def index(request):
	return render(request, 'RK_mission/h1.html')

def index2(request):
	a = AddPost.objects.all()
	# return HttpResponse(a)
	imgi = Imageshow.objects.filter(gallery='nature')
	natuimgi = Imageshow.objects.filter(gallery='landscape')
	#testi = Testinomials.objects.filter(id=3)
	#testi1 = Testinomials.objects.filter(id=2)
	testi = Testinomials.objects.all()
	lstnews = Latestnews.objects.all()
	return render(request, 'RK_mission/header.html',locals())



def author1(request):
	a_form = AddPostForm()
	if request.method == "POST":
		a_form = AddPostForm(request.POST, request.FILES)
		if a_form.is_valid():
			a_form.save()
		else:
			a_form = AddPostForm()
		return HttpResponseRedirect('/table/')
	return render(request,'RK_mission/addpost.html', locals())


def list(request):
	a = AddPost.objects.all()
	#return HttpResponseRedirect('addpost.html')
	return render(request, 'RK_mission/table.html',locals())

def add_page_list(request):
	a1 = AddPage.objects.all()
	#return HttpResponseRedirect('addpost.html')
	return render(request, 'RK_mission/add_page_list.html',locals())


def gallery(request):
	im_form = ImageForm()
	if request.method == "POST":
		im_form= ImageForm(request.POST, request.FILES)
		if im_form.is_valid():
			im_form.save()
		else:
			im_form = ImageForm()
	return render(request, 'RK_mission/gallery.html',locals())


def test(request):
	test_form = TestForm()
	if request.method == "POST":
		test_form= TestForm(request.POST)
		if test_form.is_valid():
			test_form.save()
		else:
			test = TestForm()
	return render(request, 'RK_mission/test.html',locals())


def latest_news(request):
	latest_form = latnewsForm()
	if request.method == "POST":
		latest_form = latnewsForm(request.POST)
		if latest_form.is_valid():
			latest_form.save()
		else:
			latest_form = latnewsForm()
	return render(request, 'RK_mission/latest_news.html',locals())


def sriram(request, slug):
	post_all = AddPost.objects.get(slug=slug)
	return render(request, 'RK_mission/sriram.html',locals())	


def addpage(request):
	add_pagesform = AddpageForm()
	if request.method == "POST":
		add_pagesform = AddpageForm(request.POST, request.FILES)
		if add_pagesform.is_valid():
			add_pagesform.save()
		else:
			add_pagesform = AddpageForm()
		return HttpResponseRedirect('/add_page_list')		
	return render(request, 'RK_mission/addpage.html',locals())


def about(request,slug):
	page_all = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/about.html',locals())	

def academics(request,slug):
	page_academic = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/academics.html',locals())	

def fees(request,slug):
	page_fees = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/fees.html',locals())	

def careers(request,slug):
	page_careers = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/careers.html',locals())


def admissions(request,slug):
	page_admissions = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/admissions.html',locals())	

def infrastructure(request,slug):
	page_infrastructure = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/infrastructure.html',locals())


def movement(request,slug):
	# return HttpResponse('hi')
	page_movement = AddPage.objects.get(slug=slug)
	return render(request, 'RK_mission/movement.html',locals())


def edit(request, id):
	a_form_instance = get_object_or_404(AddPost, id=id)
	a_form =AddPostForm(instance=a_form_instance)

	if request.method == 'POST':
		a_form = AddPostForm(request.POST, instance=a_form_instance)
		if a_form.is_valid():
			a_form.save()
		else:	
			a_form = AddPostForm(instance=a_form_instance)
		return HttpResponseRedirect('/table/')
	return render(request,'RK_mission/edit.html', locals())


def edit_add_page(request, id):
	a_form_instance = get_object_or_404(AddPage, id=id)
	add_pagesform =AddpageForm(instance=a_form_instance)

	if request.method == 'POST':
		add_pagesform= AddpageForm(request.POST, instance=a_form_instance)
		if add_pagesform.is_valid():
			add_pagesform.save()
		else:	
			add_pagesform = AddpageForm(instance=a_form_instance)
		return HttpResponseRedirect('/add_page_list/')
	return render(request,'RK_mission/edit_add_page.html', locals())


def domestic_donations(request):
	donations_form = DonationsForm()
	if request.method == "POST":
		donations_form = DonationsForm(request.POST)
		if donations_form.is_valid():
			donations_form.save()
		else:
			donations_form = DonationsForm()
	return render(request, 'RK_mission/domestic_donations.html',locals())


def domestic_donation_view(request):
	page_donations = Donations.objects.all()
	return render(request, 'RK_mission/domestic_donation_view.html',locals())	

def contactus(request):
	return render(request, 'RK_mission/contactus.html',locals())	


