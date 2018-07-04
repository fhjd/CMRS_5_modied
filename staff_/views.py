# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from all_models.models import *

# Create your views here.
def show_notice(request, nid=0):
    if request.method == 'GET':
        try:
            NoticeInfo.objects.get(notice_id=nid).delete()
            return HttpResponse('删除成功')
        except:
            all_notice = NoticeInfo.objects.all()
            return render(request, 'show_notice.html', {'notice': all_notice})


def show_department(request, did=0):
    if request.method == 'GET':
        try:
            DepartmentInfo.objects.get(department_id=did).delete()
            return HttpResponse('删除成功')
        except:
            departments = DepartmentInfo.objects.all()
            return render(request, 'show_department.html', {'departments':departments})


def add_notice(request):
    if request.method == 'GET':
        # 假定只有老大，和经理能发布公告
        # try:
            announcers = UserInfo.objects.filter(Q(role=UserRole.objects.get(role_name='CEO')) | Q(role=UserRole.objects.get(role_name='manager')))
            return render(request, 'add_notice.html', {'announcers': announcers})
        # except:
        #     return HttpResponse('权限限制，'
        #                         '公告发布人必须具备高级，中级权限')
    elif request.method == 'POST':
        topic = request.POST.get('topic', '')
        a = request.POST.get('a', '')
        author = UserInfo.objects.get(user_name=a)
        content = request.POST.get('content', '')
        endtime = request.POST.get('endtime', '')
        starttime = request.POST.get('starttime', '')
        print '天空不曾留下飞鸟的痕迹'
        # try:
        print '但是飞鸟已经飞过'

        NoticeInfo.objects.create(
                user=author,
                notice_item=topic,
                notice_content=content,
                notice_time=starttime,
                notice_endtime=endtime,
            )
        return HttpResponse('公告发布成功')
        # except:
        #     return HttpResponse('公告发布失败')