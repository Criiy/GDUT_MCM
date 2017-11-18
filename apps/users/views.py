# -*- encoding:UTF-8 -*-
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import UserProfile, Team
from forms import RegisterForm
from django.contrib.auth.hashers import make_password
from django.db import models
# Create your views here.
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


class RegisterView(View):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()
        imgage_url = captcha_image_url(hashkey)
        return render(request, "MCM_register.html", {"imgage_url": imgage_url, "hashkey": hashkey})

    def post(self, request):
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            stdid = request.POST.get("studentid", "")
            if UserProfile.objects.filter(username=stdid):
                return render(request, "MCM_register.html", {"reg_form": reg_form, "msg": "账号已经存在"})
            stpwd = request.POST.get("studentpwd", "")
            user = UserProfile()
            user.username = stdid
            user.password = make_password(stpwd)
            user.email = '1@1.com'
            user.save()
            return render(request, "MCM_login.html")
        else:
            return render(request, "MCM_register.html", {"msg2": "验证码错误"})


class TeamLogin(View):
    def get(self, request):
        return render(request, "MCM_login.html")

    def post(self, request):
        id = request.POST.get("studentid", "")
        pwd = request.POST.get("studentpwd", "")
        user = authenticate(username=id, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, "MCM_infopage.html")
        else:
            return render(request, "MCM_login.html", {"msg3": "账号或密码错误"})


class Info(View):
    def get(self, request):
        if request.user.is_authenticated():
            if Team.objects.filter(name=request.user.username):
                user = Team.objects.get(name=request.user.username)
                if user.gender1 == "male":
                    a = "男"
                else:
                    a = "女"
                if user.gender2 == "male":
                    b = "男"
                else:
                    b = "女"
                if user.gender3 == "male":
                    c = "男"
                else:
                    c = "女"
                return render(request, "MCM_info.html", {"user": user, "a": a, "b": b, "c": c})
            else:
                user = 0
            return render(request, "MCM_info.html", {"user": user})
        else:
            return render(request, "MCM_login.html")


class Teaminfo(View):
    def get(self, request):
        if request.user.is_authenticated():
            if Team.objects.filter(name=request.user.username):
                user = Team.objects.get(name=request.user.username)
            else:
                user = 0
            return render(request, "MCM_infopage.html", {"user": user})
        else:
            return render(request, "MCM_login.html")

    def post(self, request):
        if Team.objects.filter(name=request.user.username):       # 判断数据库中是否有该条字段的数据
            team = Team.objects.get(name=request.user.username)
        else:
            team = Team()
        name = request.user.username
        short_name1 = request.POST.get("short_name1", "")
        name1 = request.POST.get("name1", "")
        gender1 = request.POST.get("gender1")
        school1 = request.POST.get("school1", "")
        major1 = request.POST.get("major1", "")
        student_id1 = request.POST.get("student_id1", "")
        if student_id1:
            list_student_id3 = list(str(student_id1))
            cut_list1 = "20"+list_student_id3[2]+list_student_id3[3]
        else:
            cut_list1 = ""
        enrollment_year1 = cut_list1
        tel_num1 = request.POST.get("tel_num1", "")
        email1 = request.POST.get("email1", "")
        short_name2 = request.POST.get("short_name1", "")
        name2 = request.POST.get("name2", "")
        gender2 = request.POST.get("gender2")
        school2 = request.POST.get("school1", "")
        major2 = request.POST.get("major2", "")
        student_id2 = request.POST.get("student_id2", "")
        if student_id2:
            list_student_id3 = list(str(student_id2))
            cut_list2 = "20"+list_student_id3[2]+list_student_id3[3]
        else:
            cut_list2 = ""
        enrollment_year2 = cut_list2
        tel_num2 = request.POST.get("tel_num2", "")
        email2 = request.POST.get("email2", "")
        short_name3 = request.POST.get("short_name1", "")
        name3 = request.POST.get("name3", "")
        gender3 = request.POST.get("gender3")
        school3 = request.POST.get("school1", "")
        major3 = request.POST.get("major3", "")
        student_id3 = request.POST.get("student_id3", "")
        if student_id3:
            list_student_id3 = list(str(student_id3))
            cut_list3 = "20"+list_student_id3[2]+list_student_id3[3]
        else:
            cut_list3 = ""
        enrollment_year3 = cut_list3
        tel_num3 = request.POST.get("tel_num3", "")
        email3 = request.POST.get("email3", "")

                                                                                              #队员1信息录入
        team.name = name
        team.short_name1 = short_name1
        team.name1 = name1
        team.gender1 = str(gender1)
        team.school1 = school1
        team.major1 = major1
        team.student_id1 = student_id1
        team.enrollment_year1 = enrollment_year1
        team.tel_num1 = tel_num1
        team.email1 = email1
        team.save()
        team.short_name2 = short_name2                                                        #队员2信息录入
        team.name2 = name2
        team.gender2 = str(gender2)
        team.school2 = school2
        team.major2 = major2
        team.student_id2 = student_id2
        team.enrollment_year2 = enrollment_year2
        team.tel_num2 = tel_num2
        team.email2 = email2
        team.short_name3 = short_name3                                                        #队员3信息录入
        team.name3 = name3
        team.gender3 = str(gender3)
        team.school3 = school3
        team.major3 = major3
        team.student_id3 = student_id3
        team.enrollment_year3 = enrollment_year3
        team.tel_num3 = tel_num3
        team.email3 = email3
        team.save()
        return render(request, "MCM_infopage.html")
