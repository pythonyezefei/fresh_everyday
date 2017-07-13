# coding=utf-8
from django.shortcuts import redirect


# 判断用户是否登陆，通过session中的记录，只有登陆了才执行其他页面的视图
def login_decorator(func):
    def wrappedfunc(request,*args,**kwargs):
        if request.session.get('uid'):
            return func(request)
        else:
            return redirect('/login/')
    return wrappedfunc