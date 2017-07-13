from django.conf.urls import url

from ttsx_cart import views

urlpatterns = [
    url(r'^add/$',views.add),
    url(r'^count/$',views.count),
    url(r'^$',views.index),
    url(r'^change_count/$', views.change_count),
    url(r'^delete/$',views.delete),
    url(r'^order/$', views.order),
]