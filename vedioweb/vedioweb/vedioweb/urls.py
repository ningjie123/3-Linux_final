"""vedioweb URL Configuration

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
from django.contrib import admin
from django.urls import path
from web.views import login_,register,index,web1,web2,web3,web4,web5,web6

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_),
    path('register',register),
    path('index/',index),
    path('1.html',web1),
    path('2.html',web2),
    path('3.html',web3),
    path('4.html',web4),
    path('5.html',web5),
    path('6.html',web6),
    path('index.html',index),
]
