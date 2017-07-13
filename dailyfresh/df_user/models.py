# coding=utf-8
from django.db import models

# Create your models here.


#用户基本数据的模型类
class UserInfo(models.Model):
    uname = models.CharField(max_length=20,null=True)
    upasswd = models.CharField(max_length=100,null=True)
    ushou = models.CharField(max_length=20,default='',null=True)
    uemail = models.EmailField(null=True)
    utel = models.CharField(null=True, blank=True,max_length=15)
    uaddr = models.CharField(max_length=100,default='',null=True)
    upcode = models.IntegerField(null=True ,blank=True)  # 邮编
    isDelete = models.BooleanField(default=False)