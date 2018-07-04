# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from all_models.models import *
# Create your views here.
def add_staff_view(request):
    if request.method == 'GET':
        department = DepartmentInfo.objects.all()
        role = UserRole.objects.all()
        print '飞鸟：天空不曾留下我的痕迹，但是我已飞过'
        return render(request, 'add_staff.html', {'department': department, 'role': role})
    elif request.method == 'POST':
        print type(request.POST)
        try:
            department = request.POST.get('department', '')
            staff_department = DepartmentInfo.objects.get(department_name=department)
            role_name = request.POST.get('role_name', '')
            staff_power = UserRole.objects.get(role_name=role_name)
            print '谁家玉笛暗飞声'
            name = request.POST.get('name', '')
            age = request.POST.get('age', '')
            gender = request.POST.get('gender', '')
            education = request.POST.get('education', '')
            # 座机
            landline = request.POST.get('landline','')
            # 工资卡号 Payroll card number
            pcn = request.POST.get('pcn')
            # 身份证 ID card
            ic = request.POST.get('ic',)
            if UserInfo.objects.filter(user_idnum=ic):
                return HttpResponse('身份证已经登记')
            # 操作员 operator
            operator = request.POST.get('operator', '')
            account = request.POST.get('account', '')
            password = request.POST.get('password', '')
            # 民族 ethnic
            ethnic = request.POST.get('ethnic', '')
            marriage = request.POST.get('marriage', '')
            # 电话号 phone number
            pn = request.POST.get('pn', '')
            address = request.POST.get('address', '')
            hobby = request.POST.get('hobby', '')
            email = request.POST.get('email', '')

        except DepartmentInfo.DoesNotExist or UserRole.DoesNotExist:
            return HttpResponse('员工重复或注册信息不足')
            # 通过身份证号验证员工是否重复
            # UserInfo.objects.get(user_idnum=ic)
        # 创建员工表
        staff = UserInfo.objects.create(
            department=staff_department,
            role=staff_power,
            user_name=name,
            user_age=age,
            user_sex=gender,
            user_mobile=pn,
            user_address=address,
            user_idnum=ic,
            user_tel=landline,
            user_num=account,
            user_pw=password,
            user_nation=ethnic,
            user_bankcard=pcn,
            is_married=marriage,
            is_used='',
            user_diploma=education,
            user_addman=operator,
            user_intest=hobby,
            user_email=email,
        )
        return HttpResponse('员工信息，添加成功')
    else:
        return HttpResponse('添加失败')

# 添加部门
def add_department_view(request):
    if request.method == 'GET':
        return render(request, 'add_department.html')
    elif request.method == 'POST':
        department_name = request.POST.get('department_name', '')
        description = request.POST.get('description', '')
        try:
            DepartmentInfo.objects.get(department_name=department_name)
            return HttpResponse('当前部门已存在，无需创建')
        except DepartmentInfo.DoesNotExist:
            DepartmentInfo.objects.create(department_name=department_name, department_desc=description)
            return HttpResponse('恭喜，新部门创建成功')
    else:
        return HttpResponse('创建失败')


def add_role_power_view(request):
    if request.method == 'GET':

        return render(request, 'add_role_power.html')
    elif request.method == 'POST':
        role_name = request.POST.get('role', '')
        role_power = request.POST.get('power', '')
        try:
            UserRole.objects.get(role_name=role_name)
            return HttpResponse('角色名已存在')
        except UserRole.DoesNotExist:
            UserRole.objects.create(role_name=role_name, role_power=role_power)
            return HttpResponse('新建角色成功')
    else:
        return HttpResponse('创建角色失败')

