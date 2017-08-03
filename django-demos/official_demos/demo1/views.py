from django.shortcuts import render

from demo1.models import Article

def year_archive(request,year):
    year_archives=Article.objects.filter(pub_date__year=year)
    return render(request,"demo1/index.html",{"archives":year_archives})

def month_archive(request,year,month):
    month_archives=Article.objects.filter(pub_date__year=year,pub_date__month=month)
    return render(request,"demo1/index.html",{"archives":month_archives})

def day_archive(request,year,month,day):
    day_archives=Article.objects.filter(pub_date__year=year,pub_date__month=month,pub_date__day=day)
    return render(request,"demo1/index.html",{"archives":day_archives})
