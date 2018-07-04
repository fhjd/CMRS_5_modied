# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

# 客户关怀
class CustomerCare(models.Model):
    care_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('CustomerInfo', models.DO_NOTHING, blank=True, null=True)
    care_theme = models.CharField(max_length=50, blank=True, null=True)
    care_way = models.CharField(max_length=50, blank=True, null=True)
    care_time = models.DateTimeField()
    care_remark = models.CharField(max_length=1000, blank=True, null=True)
    care_nexttime = models.DateTimeField()
    care_people = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_care'

# 客户状态
class CustomerCondition(models.Model):
    condition_id = models.AutoField(primary_key=True)
    condition_name = models.CharField(max_length=50, blank=True, null=True)
    condition_explain = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_condition'

# 客户信息
class CustomerInfo(models.Model):
    customer_id = models.AutoField(primary_key=True)
    condition = models.ForeignKey(CustomerCondition, models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('CustomerSource', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('CustomerType', models.DO_NOTHING, blank=True, null=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)
    customer_sex = models.CharField(max_length=10, blank=True, null=True)
    customer_mobile = models.CharField(max_length=20, blank=True, null=True)
    customer_qq = models.CharField(max_length=20, blank=True, null=True)
    customer_address = models.CharField(max_length=500, blank=True, null=True)
    customer_email = models.CharField(max_length=100, blank=True, null=True)
    customer_remark = models.CharField(max_length=1000, blank=True, null=True)
    customer_job = models.CharField(max_length=100, blank=True, null=True)
    customer_blog = models.CharField(max_length=100, blank=True, null=True)
    customer_tel = models.CharField(max_length=20, blank=True, null=True)
    customer_msn = models.CharField(max_length=50, blank=True, null=True)
    birth_day = models.DateTimeField()
    customer_addtime = models.DateTimeField()
    customer_addman = models.CharField(max_length=50, blank=True, null=True)
    customer_changtime = models.DateTimeField()
    change_man = models.CharField(max_length=20, blank=True, null=True)
    customer_company = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_info'

# 员工信息表
class CustomerLinkman(models.Model):
    linkman_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    linkman_name = models.CharField(max_length=50, blank=True, null=True)
    linkman_sex = models.CharField(max_length=20, blank=True, null=True)
    linkman_job = models.CharField(max_length=100, blank=True, null=True)
    linkman_mobile = models.CharField(max_length=20, blank=True, null=True)
    linkman_age = models.IntegerField(blank=True, null=True)
    linkman_relation = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_linkman'

# 客户分配
class CustomerLinkreord(models.Model):
    record_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    link_time = models.DateTimeField()
    who_link = models.CharField(max_length=50, blank=True, null=True)
    link_type = models.CharField(max_length=50, blank=True, null=True)
    link_theme = models.CharField(max_length=200, blank=True, null=True)
    link_nexttime = models.DateTimeField()
    link_remark = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_linkreord'

# 客户来源
class CustomerSource(models.Model):
    source_id = models.AutoField(primary_key=True)
    source_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_source'

# 客户类型
class CustomerType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'customer_type'

# 部门信息
class DepartmentInfo(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=50, blank=True, null=True)
    department_desc = models.CharField(max_length=500, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'department_info'

# 邮件表
class EmailInfo(models.Model):
    email_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(CustomerInfo, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    email_content = models.CharField(max_length=2000, blank=True, null=True)
    email_time = models.DateTimeField()
    email_state = models.CharField(max_length=50, blank=True, null=True)
    email_theme = models.CharField(max_length=200, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'email_info'

# 房屋信息
class HouseInfo(models.Model):
    house_id = models.AutoField(primary_key=True)
    type = models.ForeignKey('HouseType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    house_address = models.CharField(max_length=500, blank=True, null=True)
    house_price = models.IntegerField(blank=True, null=True)
    house_ambient = models.CharField(max_length=1000, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'house_info'

# 房屋类型
class HouseType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'house_type'

# 公告表
class NoticeInfo(models.Model):
    notice_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserInfo', models.DO_NOTHING, blank=True, null=True)
    notice_item = models.CharField(max_length=100, blank=True, null=True)
    notice_content = models.CharField(max_length=2000, blank=True, null=True)
    notice_time = models.DateTimeField()
    notice_endtime = models.DateTimeField()
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'notice_info'

# 添加员工表
class UserInfo(models.Model):
    # 自动生成id
    user_id = models.AutoField(primary_key=True)
    # 部门
    department = models.ForeignKey(DepartmentInfo, models.DO_NOTHING, blank=True, null=True)
    # 角色权限
    role = models.ForeignKey('UserRole', models.DO_NOTHING, blank=True, null=True)
    # 姓名
    user_name = models.CharField(max_length=50, blank=True, null=True)
    user_sex = models.CharField(max_length=10, blank=True, null=True)
    # 手机
    user_mobile = models.CharField(max_length=20, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    user_address = models.CharField(max_length=500, blank=True, null=True)
    # 账户
    user_num = models.CharField(max_length=100, blank=True, null=True)
    # 密码
    user_pw = models.CharField(max_length=50, blank=True, null=True)
    # 座机
    user_tel = models.CharField(max_length=20, blank=True, null=True)
    # 身份证
    user_idnum = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    user_addtime = models.DateTimeField(auto_now_add=True)
    user_addman = models.CharField(max_length=50, blank=True, null=True)
    user_changetime = models.DateTimeField(auto_now=True)
    user_changeman = models.CharField(max_length=50, blank=True, null=True)
    # 爱好
    user_intest = models.CharField(max_length=1000, blank=True, null=True)
    # 学历
    user_diploma = models.CharField(max_length=20, blank=True, null=True)
    # 银行卡
    user_bankcard = models.CharField(max_length=20, blank=True, null=True)
    # 民族
    user_nation = models.CharField(max_length=20, blank=True, null=True)
    # 婚否
    is_married = models.CharField(max_length=10, blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'user_info'

# 员工权限表
class UserRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    # 老板  管理员  员工
    role_name = models.CharField(max_length=50, blank=True, null=True)
    # 1  2  3
    role_power = models.IntegerField(blank=True, null=True)
    is_used = models.CharField(max_length=10, blank=True, null=True)

    class Meta:

        db_table = 'user_role'