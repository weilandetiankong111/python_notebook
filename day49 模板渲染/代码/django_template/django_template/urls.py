"""django_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^index2/', views.index2),

    url(r'^csrf/', views.csrf),


    url(r'^t1/', views.t1),
    url(r'^t2/', views.t2),
    url(r'^t3/', views.t3),

    url(r'^zujian/', views.zujian),
    url(r'^tan/', views.tan),
    url(r'^bb/', views.bb),

    url(r'^basic/', views.basic),


]
