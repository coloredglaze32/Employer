from django.shortcuts import render, redirect
from app.models import Department, UserInfo

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

def edit_list(request, nid):
    # 修改部门
    obj = Department.objects.filter(id=nid).first()
    if request.method == "GET":
        return render(request,"edit_list.html", {"obj":obj})
    
    title = request.POST.get("title")
    Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list")

def delete_list(request):
    nid = request.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list")

def user_list(request):
    # 用户列表
    userList = UserInfo.objects.all()
    
    return render(request, "user_list.html", {"userList":userList})

from django import forms

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ["name", "age", "password", "account", "gender", "depart_id", "create_time"]
        widgets = {
            "create_time":forms.DateTimeInput(attrs={"type":"datetime-local"}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

def add_user(request):
    if request.method == "GET":
        user_form = UserInfoForm()
        return render(request, "add_user.html", {"user_form":user_form})
    
    # 校验
    form = UserInfoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    return render(request, "add_user.html", {"form":form})

def delete_user(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list")

def edit_user(request, nid):
    row_object = UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserInfoForm(instance=row_object)
        
        return render(request, "edit_user.html", {"form":form})
        
    form = UserInfoForm(request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user/list")
    return render(request, "edit_user.html", {"form":form})

