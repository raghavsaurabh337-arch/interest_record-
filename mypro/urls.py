"""
URL configuration for recode project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from mypro import front_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',front_views.home,name='home'),
    path('navbar/',front_views.navbar,name='navbar'),
    path('recode/',front_views.recode,name='recode'),
    path('calculate/',front_views.calculate,name='calculate'),
    path('search/', front_views.search_record, name='search_record'),
    path('edit_recode/<int:id>/',front_views.edit,name='edit'),
    path('delete_recode/<int:id>/',front_views.delete,name='delete'),
]
