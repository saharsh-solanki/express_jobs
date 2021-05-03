"""job_env URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from job_management import views

urlpatterns = [
    path('', views.managerlogin, name="managerlogin"),
    path('managerlogin', views.managerlogin, name="managerlogin"),
    path('manager_dashboard',views.main,name="manager_dashboard"),
    path('deletemaincategory', views.deletemaincategory, name="deletemaincategory"),
    path('deletesubcategory', views.deletesubcategory, name="deletesubcategory"),
    path('deletesubsubcategory', views.deletesubsubcategory, name="deletesubsubcategory"),
    path('maincategory', views.maincategory, name="maincategory"),
    path('subcategory', views.subcategory, name="subcategory"),
    path('subsubcategory', views.subsubcategory, name="subsubcategory"),
    path('addjob', views.addjob, name="addjob"),
    path('doaddmaincategory', views.doaddmaincategory, name="doaddmaincategory"),
    path('doaddsubcategory', views.doaddsubcategory, name="doaddsubcategory"),
    path('doaddsubsubcategory', views.doaddsubsubcategory, name="doaddsubsubcategory"),
    path('doaddjob', views.doaddjob, name="doaddjob"),
    path('viewjob', views.viewjob, name="viewjob"),
    path('delete', views.delete, name="delete"),
    path('updatejob<id>', views.updatejob, name="updatejob"),
    path('doupdatejob<id>', views.doupdatejob, name="doupdatejob"),
    path('logout',views.logout,name='logout'),
]
