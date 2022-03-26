"""clg_data URL Configuration

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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from clg_dataapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/',views.StudentsView.as_view()),

    path('api/branches/',views.branchView.as_view()),
    path('api/teachers/',views.teacherView.as_view()),
    path('api/student/<int:tid>',views.StudentView.as_view())
]
