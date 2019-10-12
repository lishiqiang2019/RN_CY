from django.http import HttpResponse
from django.shortcuts import render,redirect
from dine import models
from .models import user_info
from .models import Food_info
from .models import Order

def index(request):#首页
    return HttpResponse('Hello,world.You are looking at the dine index.')

def dine_info(request):
    return HttpResponse('hello ,this dine information page')

def login(request):#登录页面
    username = request.GET.get('username')
    password = request.GET.get('password')
    if username.strip() and password:
        try:
            user = models.user_info.objects.get(user_name=username)
        except:
            return HttpResponse('用户不存在')
        if user.password == password:
            return redirect('/index/')
        else:
            return HttpResponse('密码错误')

def register(request):#注册页面
    user1 = user_info()
    user1.user_name = request.GET.get('username')
    user1.user_pwd = request.GET.get('password')
    pwds = request.GET.get('passwords')
    user1.user_phone = request.GET.get('phone')

    # filterResult1 = user_info.objects.filter(username=user1.user_name)
    # filterResult2 = user_info.objects.filter(phone=user1.user_phone)
    # if len(filterResult2)>0:
    #     return HttpResponse("手机号已被使用")
    # if len(filterResult1)>0:
    #     return HttpResponse("用户名重复")

    user1.save()
    return HttpResponse("注册成功")
def food_order(request):
    print(request.GET.get)
    return HttpResponse("菜品界面")
def speicfic_info(request):
    sp_info = user_info()
    sp_info.user_phone = request.GET.get('')
    sp_info.user_address = request.GET.get('')
    sp_info.save()
def paycar(request):
    pass