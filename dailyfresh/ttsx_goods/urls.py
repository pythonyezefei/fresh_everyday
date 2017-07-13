# coding=utf-8
from django.conf.urls import url
import views
from ttsx_goods.search_view import MySearchView

urlpatterns = [
    url(r'^$', views.index),
    url(r'^detail(\d+)/$',views.detail),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.goods_list),
    url(r'^search/$', MySearchView.as_view()),
]