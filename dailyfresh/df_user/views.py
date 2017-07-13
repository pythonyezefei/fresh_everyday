# coding=utf-8
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from hashlib import sha1
import datetime
import django.forms

from ttsx_goods.models import GoodsInfo
from user_decorator import login_decorator
from df_user.models import UserInfo
# Create your views here.


# 跳转用户注册页面
def register(request):
    content = {'title':'注册','flag':'0'}

    return render(request, 'df_user/register.html', content)


# 获取注册表单页面提交的信息
def register_action(request):
    uname = request.POST.get('user_name')
    upwd = request.POST.get('pwd')
    uemail = request.POST.get('email')
    users = UserInfo.objects.all()
    nameList = []
    s = sha1()
    s.update(upwd)
    upwd_sha1 = s.hexdigest()
    for temp in users:
        nameList.append(temp.uname)
    if uname not in nameList :
        user = UserInfo()
        user.uname = uname
        user.upasswd = upwd_sha1
        user.uemail = uemail
        user.save()
        return HttpResponse('ok')
    else:
        return HttpResponse('已经注册过，请直接登陆')


# 用户登陆页面显示
def login(request):
    uname = request.COOKIES.get('uname')
    return render(request, 'df_user/login.html',{'uname': uname,'title':'登陆', 'flag':'0'})


# 验证用户的输入
def login_check(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')
    remember = request.POST.get('remember',0)
    nameList = []
    users = UserInfo.objects.all()
    for temp in users:
        nameList.append(temp.uname)
    if name in nameList:
        user = UserInfo.objects.get(uname=name)
        passwd = user.upasswd
        s = sha1()
        s.update(pwd)
        pwd_sha1 =s.hexdigest()
        if pwd_sha1 == passwd:
            response = redirect('/center/')
            if remember == '1':
                response.set_cookie('uname',name, expires=datetime.datetime.now()+datetime.timedelta(days=7)) # 写入cookie，　设置过期时间
            else:
                response.set_cookie('uname', name, expires=-1)

            user = UserInfo.objects.get(uname=name)
            id = user.id
            uname = user.uname
            request.session['uid'] = id
            request.session['uname'] = uname
            request.session.set_expiry(0)  # 设置浏览器关闭即失效
            return response

        else:
            content = {'pwd_error':'密码错误'}
            return render(request, 'df_user/login.html/',content)
    else:
        content = {'name_error':'用户名不存在'}
        return render(request,'df_user/login.html/',content)

# 退出登陆
def logout(request):
    request.session.flush()
    return redirect('/login/')

@login_decorator
# 显示用户中心页面
def center(request):
    user = UserInfo.objects.get(pk=request.session['uid'])

    resultlist = request.COOKIES.get('goods_id','').split(',')[:-1]
    goodslist = []
    for num in resultlist:
        goodslist.append(GoodsInfo.objects.get(id=num))
    content = {'user':user,'title':'用户中心', 'goodslist':goodslist,'flag1':'-1'}
    return render(request, 'df_user/user_center_info.html',content)
@login_decorator
def center_order(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    content = {'user': user, 'title': '用户中心','flag1':'-1'}
    return render(request, 'df_user/user_center_order.html',content)
@login_decorator
def center_site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        ushou = post.get('ushou')
        uaddr = post.get('uaddr')
        upcode = post.get('upcode')
        utel = post.get('uphone')
        user.ushou = ushou
        user.uaddr = uaddr
        user.upcode = upcode
        user.utel = utel
        user.save()
    content = {'user': user,'flag1':'-1'}
    return render(request, 'df_user/user_center_site.html', content)

# 忘记密码
def forgetpwd(request):

    return render(request, 'df_user/forget.html',{'flag1':'-1'})

def islogin(request):
    result = request.session.has_key('uid')
    return JsonResponse({'islogin':result})

