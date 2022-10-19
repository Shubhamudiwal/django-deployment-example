from django.contrib import admin
from django.urls import path,re_path
from AppTwo import views
from django.conf.urls import include

urlpatterns = [
    re_path(r'^$',views.user,name = 'user')
]
