# -*- encoding:UTF-8 -*-
from __future__ import unicode_literals
import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

today = datetime.date.today()
y = today.year


class UserProfile(AbstractUser):
    pass

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Team(models.Model):
    name = models.CharField(max_length=30, default="", verbose_name='账号')
    # years = models.CharField(max_length=4, default=y, verbose_name=u'参赛年份')
    # area_code = models.CharField(max_length=2, default='19', verbose_name=u'区号')
    # college_num = models.CharField(max_length=3, default='008', verbose_name=u'学校编号')
    # school_num = models.CharField(max_length=3, default='', verbose_name=u'校内编号')
    # college_name = models.CharField(max_length=30, default=u'广东工业大学', verbose_name=u'学校名称')
    # participant_type = models.CharField(max_length=10, default=u'本科组', verbose_name=u'参赛组类型')
    short_name1 = models.CharField(max_length=30, default="", verbose_name="姓名缩写")
    name1 = models.CharField(max_length=10, default='', verbose_name=u'姓名1', blank=True)
    gender1 = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default="male",
                               verbose_name="性别1")
    school1 = models.CharField(max_length=30, default="", verbose_name="学院")
    major1 = models.CharField(max_length=40, default='', verbose_name=u'专业1', blank=True)
    student_id1 = models.CharField(max_length=10, default='', verbose_name=u'学号1', blank=True)
    enrollment_year1 = models.CharField(max_length=4, default='', verbose_name=u'入学年份1', blank=True)
    tel_num1 = models.CharField(max_length=11, default='', verbose_name=u'电话1', blank=True)
    email1 = models.EmailField(max_length=30, verbose_name='email1', blank=True)
    short_name2 = models.CharField(max_length=30, default="", verbose_name="姓名缩写")
    name2 = models.CharField(max_length=10, default='', verbose_name=u'姓名2', blank=True)
    gender2 = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default="male",
                               verbose_name="性别2")
    school2 = models.CharField(max_length=30, default="", verbose_name="学院")
    major2 = models.CharField(max_length=40, default='', verbose_name=u'专业2', blank=True)
    student_id2 = models.CharField(max_length=10, default='', verbose_name=u'学号2', blank=True)
    enrollment_year2 = models.CharField(max_length=4, default='', verbose_name=u'入学年份2', blank=True)
    tel_num2 = models.CharField(max_length=11, default='', verbose_name=u'电话2', blank=True)
    email2 = models.EmailField(max_length=30, verbose_name='email2', blank=True)
    short_name3 = models.CharField(max_length=30, default="", verbose_name="姓名缩写")
    name3 = models.CharField(max_length=10, default='', verbose_name=u'姓名3', blank=True)
    gender3 = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default="male",
                               verbose_name="性别3")
    school3 = models.CharField(max_length=30, default="", verbose_name="学院")
    major3 = models.CharField(max_length=40, default='', verbose_name=u'专业3', blank=True)
    student_id3 = models.CharField(max_length=10, default='', verbose_name=u'学号3', blank=True)
    enrollment_year3 = models.CharField(max_length=4, default='', verbose_name=u'入学年份3', blank=True)
    tel_num3 = models.CharField(max_length=11, default='', verbose_name=u'电话3', blank=True)
    email3 = models.EmailField(max_length=30, verbose_name='email3', blank=True)
    # teacher = models.CharField(max_length=10, verbose_name=u'教师姓名')
    # teach_title = models.CharField(max_length=20,
    #                                choices=(('lecturer', u'讲师'), ('professor', u'教授'), ('vice_professor', u'副教授')),
    #                                default="")
    # mobile = models.CharField(max_length=11, null=True, blank=True)
    # teach_email = models.EmailField(max_length=30, verbose_name=u'教师Email')
    # remarks = models.CharField(max_length=200, verbose_name=u'备注')

    class Meta:
        verbose_name = u'队伍信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name1
