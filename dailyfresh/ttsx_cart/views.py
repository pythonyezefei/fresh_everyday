#coding=utf-8
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from df_user.models import UserInfo
from df_user.user_decorator import login_decorator
from ttsx_cart.models import CartInfo


def add(request):
    try:
        gid = int(request.GET.get('gid'))
        uid = int(request.session.get('uid'))
        count = int(request.GET.get('count','1'))
        cart = CartInfo.objects.filter(goods_id=gid,user_id=uid)
        if len(cart) == 1:
            cart1 = cart[0]
            cart1.count += count
            cart1.save()
        else:
            cart = CartInfo()
            cart.goods_id = gid
            cart.user_id = uid
            cart.count = count
            cart.save()
        return JsonResponse({'isadd':1})
    except:
        return JsonResponse({'isadd':0})

def count(request):
    uid = request.session.get('uid')
    count = CartInfo.objects.filter(user_id=uid).count()
    return JsonResponse({'count':count})

@login_decorator
#　购物车页面
def index(request):
    uid = request.session.get('uid')
    cart_list = CartInfo.objects.filter(user_id=uid)
    context = {'title':'购物车页面','cart_list':cart_list}
    return render(request,'ttsx_cart/cart.html' ,context)

def change_count(request):
    try:
        id = int(request.GET.get('id'))
        num =int(request.GET.get('num'))
        cart = CartInfo.objects.get(pk=id)
        cart.count = num
        cart.save()

        return JsonResponse({'ok':1})
    except:
        return JsonResponse({'ok':0})

def delete(request):
    id = int(request.GET.get('id'))
    cart = CartInfo.objects.get(pk=id)
    cart.delete()
    return JsonResponse({'ok':1})


def order(request):
    uid = request.session['uid']
    user = UserInfo.objects.get(id=int(uid))
    cartid = request.POST.getlist('cart_id')
    cartlist = CartInfo.objects.filter(id__in=cartid)
    context = {'title':'订单页','user':user,'cartlist':cartlist}

    return render(request, 'ttsx_cart/order.html',context)


