"""mcm3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
# from django.contrib import admin
# from django.views.generic import TemplateView
from users.views import TeamLogin, RegisterView, Teaminfo, Info
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^$', TeamLogin.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^Teaminfo/$', Teaminfo.as_view(), name='Teaminfo'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^info/$', Info.as_view(), name='info'),
]