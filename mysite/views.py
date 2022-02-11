from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
	home = "<h2>大家好，歡迎</h2><hr>"
	now = datetime.datetime.now()
	home = home + "現在時間:"+str(now)
	return HttpResponse(home)

def showdate(request):

	now = datetime.datetime.now()
	return HttpResponse("現在時間:"+str(now))