"""
URL configuration for patient_doctor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Signup import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index),
    path("login",views.index),
    #path("register1",views.register),
    #path('newUser',views.register),
    path("dashboard_pt",views.dashboard_pt),
    path("dashboard_dt",views.dashboard_dt),
    path("reg",views.reg),
    path("display",views.display),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
