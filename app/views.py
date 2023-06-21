from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_Topic(request):
    tn=input('enter a name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserted')

def insert_Webpage(request):
    tn=input('enter a name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter a name')
    r=input('enter a url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=r)[0]
    WO.save()
    return HttpResponse('Webpage is inserted')



