from django.shortcuts import render, redirect
from app.models import Department

# Create your views here.

def depart_list(request):
    # 部门列表

    # 去数据库中获取所有的部门列表
    departList = Department.objects.all()

    return render(request, "depart_list.html",{"departList":departList})

def add_list(request):

    # 添加部门

    if request.method == "GET":
        return render(request, "add_list.html")
    title = request.POST.get("title")
    Department.objects.create(title=title)
    return redirect("/depart/list")