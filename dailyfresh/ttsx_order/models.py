# coding=utf-8
from django.db import models
# Create your models here.
from df_user.models import UserInfo
from ttsx_goods.models import GoodsInfo


class OrderMain(models.Model):
    orderid = models.CharField(max_length=20,primary_key=True)  # 自定义一个主键　2017713000000uid　作为订单号
    order_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserInfo)
    total = models.DecimalField(max_digits=8,decimal_places=2)
class OrderDetail(models.Model):
    order = models.ForeignKey(OrderMain)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
