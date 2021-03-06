"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

# import 할 때는 py파일까지 해야 한다!!
import bbs.views
import member.views

# urls.py에는 주소 하나당 함수 하나를 연결
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member.views.index),
    path('member/', member.views.start),
    path('member/index1', member.views.index1),
    path('member/index2', member.views.index2),
    path('member/index3', member.views.index3),
    path('bbs/', bbs.views.start),
    path('bbs/index', bbs.views.index),
    path('bbs/insert', bbs.views.insert),
    path('bbs/insert2', bbs.views.insert2),
    path('bbs/update', bbs.views.update),
    path('bbs/update2', bbs.views.update2)
]
