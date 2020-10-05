"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from proapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',views.registration_view),
    path('',views.Login_View),
    path('home/',views.home_view),
    path('feedback/',views.feedback_view),
    path('contact/',views.contact_view),
    path('services/',views.service_view),
    path('Python/',views.python_view),
    path('Django/',views.django_view),
    path('UI/',views.ui_view),
    path('RESTAPI/',views.restapi_view),
    path('gallery/',views.gallery_view),
    path('contact_us/',views.contact_us_view)
]
