from django.shortcuts import render
from django.http import HttpResponse
from demo.models import Person
from demo.user import User
def sayHello(request):
    return HttpResponse("Hello World")

def add(request):
    a=request.GET.get("a",0)
    b=request.GET.get("b",0)
    c=int(a)+int(b)
    return HttpResponse(str(c))

def msg(request):
    return render(request,"demo/message.html")

def template1(request):
    return render(request,"demo/template1.html")

def template2(request):
    return render(request,"demo/template2.html")

def template3(request):
    str1="这是第一个字符串"
    str2="这是第二个字符串"
    return render(request,"demo/template3.html",{"str1":str1,"str2":str2})

def template4(request):
    myList=["one","two","three","four","five"]
    return render(request,"demo/template4.html",{"myList":myList})

def create(request):
    # 第一种方式
    # p=Person.objects.create(name="Jack",age=18)
    # return HttpResponse(p.name+","+str(p.age))    

    # 第二种方式
    # p=Person(name="Rose",age=16)
    # p.save()
    # return HttpResponse(p.name+","+str(p.age))

    # 第三种方式
    p1=Person.objects.get_or_create(name="Jack",age=22) 
    p2=Person.objects.get_or_create(name="Lisa",age=16)
    str1=str("新建" if p1[1]==True else "取出")+":"+p1[0].name+","+str(p1[0].age)
    str2=str("新建" if p2[1]==True else "取出")+":"+p2[0].name+","+str(p2[0].age)
    return HttpResponse(str1+","+str2)

def delete(request):
    # 删除name为Tom的记录
    # p=Person.objects.get(name="Tom")
    # r=p.delete()
    # return HttpResponse("删除"+str(r[0])+"条记录")    

    # 删除年龄为18的所有记录
    # r=Person.objects.filter(age=18).delete()
    # return HttpResponse("删除"+str(r[0])+"条记录")

    # 删除Person模型对应的表中的所有记录
    r=Person.objects.all().delete()
    return HttpResponse("删除"+str(r[0])+"条记录")

def update(request):
    # 方法一
    # p=Person.objects.get(name="Tom")
    # p.age=39
    # p.save()
    # return HttpResponse("更新成功")    
    
    # 方法二
    Person.objects.filter(name="Tom").update(age=93)
    return HttpResponse("更新成功")

def research(request):
    # 例1 查询所有姓名
    # result=""
    # querySet=Person.objects.all()
    # for item in querySet:
    #    result+=item.name+" "
    # return HttpResponse(result)

    # 例2
    # result=""
    # querySet=Person.objects.all().values()
    # for item in querySet:
    #    print(item)
    #    result+=str(item)
    # return HttpResponse(result)

    # 例3
    # p=Person.objects.get(name="Tom")
    # return HttpResponse(p.name+","+str(p.age)) 

    # 例4
    # result=""
    # querySet=Person.objects.filter(age=18)
    # for item in querySet:
    #    print(item.name+","+str(item.age))
    #    result+=item.name+","+str(item.age)+" "
    # return HttpResponse(result)

    # 例5
    # result=""
    # querySet=Person.objects.filter(name__contains="Ja")
    # for item in querySet:
    #    print(item.name+","+str(item.age))
    #    result+=item.name+","+str(item.age)+" "
    # return HttpResponse(result)

    # 例6
    # result=""
    # querySet=Person.objects.order_by("age")
    # for item in querySet:
    #    print(item.name+","+str(item.age))
    #    result+=item.name+","+str(item.age)+" "
    # return HttpResponse(result) 

    # 例7
    # result=""
    # querySet=Person.objects.order_by("-age")
    # for item in querySet:
    #    print(item.name+","+str(item.age))
    #    result+=item.name+","+str(item.age)+" "
    # return HttpResponse(result)

    # 例8
    result=""
    querySet=Person.objects.order_by("-age")
    for item in querySet[:3]:
        print(item.name+","+str(item.age))
        result+=item.name+","+str(item.age)+" "
    return HttpResponse(result)

def getInfo(request):
    if request.method=="GET":
        username=request.GET.get("username",None)
        age=request.GET.get("age",None)
    elif request.method=="POST":
        username=request.POST.get("username",None)
        age=request.POST.get("age",None)
    return HttpResponse(username+","+str(age))

def form1(request):
    return render(request,"demo/form1.html")

def index(request):
    if request.method=="POST" or "GET":
        if request.method=="POST":
            userForm=User(request.POST)
        else:
            userForm=User(request.GET)
        if userForm.is_valid():
            username=userForm.cleaned_data["username"]
            age=userForm.cleaned_data["age"]
            return HttpResponse(username+","+str(age))
    else:
        userForm=User()
    return render(request,"demo/index.html",{"form":userForm})
