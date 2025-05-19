"""
URL configuration for Employer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # 部门管理
    path("depart/list", views.depart_list),
    path("add/list", views.add_list),
    path("edit/<int:nid>/list", views.edit_list),
    path("delete/list", views.delete_list),
    
    # 用户管理
    path("user/list", views.user_list),
    path("add/user", views.add_user),
    path("delete/user", views.delete_user),
    path("edit/<int:nid>/user", views.edit_user),
    
    # 靓号管理
    path("pretty/list", views.pretty_list),
    path("pretty/add", views.add_pretty),
    path("pretty/<int:nid>/edit", views.edit_pretty),
    path("pretty/<int:nid>/delete", views.delete_pretty),
]
