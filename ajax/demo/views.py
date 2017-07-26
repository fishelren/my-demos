from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from demo.forms import StudentForm
from demo.models import Student
import json
# Create your views here.

def index(request):
    studentForm=StudentForm()
    studentList=Student.objects.all()
    return render(request,"./demo/index.html",{"studentForm":studentForm,"studentList":studentList})

@csrf_exempt
def add(request):
    stuObj=json.loads(request.body) # 将post方式包含在请求体中的json字符串转换为python对象
    try:
        Student.objects.create(username=stuObj["username"],age=stuObj["age"]) # python中字典只能通过中括号来引用键，而不能用点号
        studentList=Student.objects.all()
        studentListRendering=render_to_string("demo/studentList.html",{"studentList":studentList}) # 更新模板
        return JsonResponse({"status":"ok","studentListRendering":studentListRendering}) 
    except:
        return JsonResponse({"status":"error"})
        
    
