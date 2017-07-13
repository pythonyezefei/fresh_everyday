# coding=utf-8
from django.shortcuts import render, redirect
from ttsx_goods.models import GoodsInfo, TypeInfo
from django.core.paginator import Paginator
# Create your views here.


# 显示首页，查询商品数据传递给首页
def index(request):
    typelist = TypeInfo.objects.all()
    list = []
    for type1 in typelist:
        newlist = type1.goodsinfo_set.order_by('-id')[0:4]
        clicklist = type1.goodsinfo_set.order_by('-gclick')[0:4]
        list.append({'newlist':newlist,'clicklist':clicklist,'t1':type1})
    context = {'title':'首页','list':list}
    return render(request, 'ttsx_goods/index.html', context)


# 商品列表页显示
def goods_list(request,tid, pindex, sid):
    t1 = TypeInfo.objects.get(pk=int(tid))
    newlist = t1.goodsinfo_set.order_by('-id')[0:2]
    sid = int(sid)
    num = request.GET.get('p', '1')
    if sid == 1:
        orderbystr = '-id'
    elif sid == 2:
        if num == '1':
            orderbystr = '-gprice'
            num = '-1'
        else:
            orderbystr = 'gprice'
            num = '1'
    else:
        orderbystr = '-gclick'
    glist = t1.goodsinfo_set.order_by(orderbystr)
    p = Paginator(glist,5)
    page = p.page(pindex)
    context = {'title':'商品列表','flag1':'0','t1':t1,'newlist':newlist,'page':page,'sid':sid,'num':num}
    return render(request, 'ttsx_goods/list.html',context)


# 商品详情页展示
def detail(request, gid):
    try:
        goods = GoodsInfo.objects.get(id=int(gid))
        # 多查一,然后再用一查多，找到所有此商品分类中最新的两个商品
        newlist = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
        goods.gclick += 1
        goods.save()
        context = {'goods':goods,'newlist':newlist,'title':'商品详情'}
        response = render(request,'ttsx_goods/detail.html',context)
        ids = request.COOKIES.get('goods_id','').split(',')
        if gid in ids:
            ids.remove(gid)
        ids.insert(0,gid)
        if len(ids) > 6:
            ids.pop()
        response.set_cookie('goods_id',','.join(ids),max_age=60*60*24*7)
        return response
    except:
        return render(request,'404.html')
