#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^top.html$', views.top_view),
    url(r'^left.html$', views.left_view),
    url(r'^down.html$', views.down_view),
]