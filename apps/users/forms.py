# -*- coding:utf-8 -*- 
__auther__ = 'Zins'
__date__ = '2017/11/6 16:53'


from django import forms
from captcha.fields import CaptchaField
# from .forms import UserProfile


class RegisterForm(forms.Form):
    studentid = forms.CharField(required=True)
    studentpwd = forms.CharField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class TeaminfoForm(forms.Form):
    name = forms.CharField(required=True)
    name1 = forms.CharField(required=True)
    gender1 = forms.CharField(required=True)
    major1 = forms.CharField(required=True)
    student_id1 = forms.CharField(required=True)
    enrollment_year1 = forms.CharField(required=True)
    tel_num1 = forms.CharField(required=True)
    email1 = forms.EmailField(required=True)
    name2 = forms.CharField(required=True)
    gender2 = forms.CharField(required=True)
    major2 = forms.CharField(required=True)
    student_id2 = forms.CharField(required=True)
    enrollment_year2 = forms.CharField(required=True)
    tel_num2 = forms.CharField(required=True)
    email2 = forms.EmailField(required=True)
    name3 = forms.CharField(required=True)
    gender3 = forms.CharField(required=True)
    major3 = forms.CharField(required=True)
    student_id3 = forms.CharField(required=True)
    enrollment_year3 = forms.CharField(required=True)
    tel_num3 = forms.CharField(required=True)
    email3 = forms.EmailField(required=True)
