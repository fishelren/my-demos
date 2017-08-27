from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

def index(request):
    myList=["good","good","study","day","day","up"]
    return render(request,"demo/test.html",{"myList":json.dumps(myList)})

def test2(request):
    return render(request,"demo/test2.html")

def getData(request):
    list2 = ['tomorrow', 'is', 'another', 'day']
    return JsonResponse({'list2':list2})