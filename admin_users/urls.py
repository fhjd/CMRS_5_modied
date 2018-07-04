#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    # 添加员工信息
    url(r'^$', views.add_staff_view),
    # 添加部门信息
    url(r'^add_department/$', views.add_department_view),
    url(r'^add_role_power/$', views.add_role_power_view),
]