# -*- coding:utf-8 -*- 
__auther__ = 'Zins'
__date__ = '2017/11/9 17:23'


import xadmin
from .models import Team
from xadmin import views


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u'美赛报名管理系统'
    site_footer = u'广东工业大学校内网'


class TeamAdmin(object):
    list_display = ["name1", "gender1", "major1", "student_id1", "enrollment_year1", "tel_num1", "email1",
                    "name2", "gender2", "major2", "student_id2", "enrollment_year2", "tel_num2", "email2",
                    "name3", "gender3", "major3", "student_id3", "enrollment_year3", "tel_num3", "email3"]
    search_fields = ["name1", "gender1", "major1", "student_id1", "enrollment_year1", "tel_num1", "email1",
                    "name2", "gender2", "major2", "student_id2", "enrollment_year2", "tel_num2", "email2",
                    "name3", "gender3", "major3", "student_id3", "enrollment_year3", "tel_num3", "email3"]


# class UserProfileAdmin(object):
#     pass


xadmin.site.register(Team, TeamAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)