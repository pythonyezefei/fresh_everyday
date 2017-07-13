from django.db import models

# Create your models here.
from df_user.models import UserInfo
from ttsx_goods.models import GoodsInfo


class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()