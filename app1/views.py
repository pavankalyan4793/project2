from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1><marquee direction="left" height=100%>virat is a good batsmen</marqee></h1>')
def virat1(request):
    return HttpResponse('<h1><marquee direction="up" height=100%>virat is a good batsmen</marqee></h1>')