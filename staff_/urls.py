#coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^show_notice/(\d*)', views.show_notice),
    url(r'^show_department/(\d*)', views.show_department),
    url(r'^add_notice/', views.add_notice),
]