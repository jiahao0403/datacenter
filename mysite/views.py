from django.shortcuts import render
from django.http import HttpResponse
import datetime
import jieba

stopwords=list()
with open("stopwords.txt","rt",encoding = "utf-8") as fp:
    	stopwords = [word.strip() for word in fp.readlines()]

def index(request):

	home = "<h2>大家好，歡迎</h2><hr>"
	now = datetime.datetime.now()
	home = home + "現在時間:"+str(now)
	return HttpResponse(home)

def showdate(request):

	now = datetime.datetime.now()
	return HttpResponse("現在時間:"+str(now))

def poem(request):
	f = open("poem.txt","r", encoding="utf-8").read()

	jieba.load_userdict('dict.txt')

	words = jieba.lcut(f)
	data = [data for data in words if data not in stopwords]
	data = ",".join(data)
	return HttpResponse(data)
