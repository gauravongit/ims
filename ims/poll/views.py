from django.shortcuts import render
import requests
from django.http import *
from django.template.loader import get_template
from django.template import Context
# Create your views here.
def welcome(request):
	return render(request,'welcome.html')
	#return HttpResponse("hello world")