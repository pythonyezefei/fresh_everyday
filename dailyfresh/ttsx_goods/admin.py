from django.contrib import admin

# Register your models here.
from models import *


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']
admin.site.register(TypeInfo,TypeAdmin)

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id','gtitle','gprice','gclick']
    list_per_page = 15

admin.site.register(GoodsInfo,GoodsAdmin)
