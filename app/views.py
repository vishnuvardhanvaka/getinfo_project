from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request,'home.html')
def mobile(request):
	return render(request,'mobile.html')
def laptop(request):
	return render(request,'laptop.html')
def tv(request):
	return render(request,'tv.html')

