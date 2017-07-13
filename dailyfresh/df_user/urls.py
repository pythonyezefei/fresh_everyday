# coding=utf-8
from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_action/$', views.register_action),
    url(r'^login/$', views.login),
    url(r'^login_check/$', views.login_check),
    url(r'^center/$' ,views.center),
    url(r'^center/order/$' ,views.center_order),
    url(r'^center/site/$' ,views.center_site),
    url(r'^logout/$', views.logout),
    url(r'^forgetpwd/$', views.forgetpwd),
    url(r'^islogin/$', views.islogin),

]