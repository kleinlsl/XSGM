"""XSGM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from XSGM.settings import STATIC_ROOT
from app.views import UserView, GradeView, MessageView, CourseView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('user/', UserView.as_view(), name="user"),
    path('grade/',GradeView.as_view(),name='grade'),
    path('message/',MessageView.as_view(),name="message"),
    path('course/', CourseView.as_view(), name="course"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
]
