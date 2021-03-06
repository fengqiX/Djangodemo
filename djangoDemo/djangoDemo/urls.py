"""djangoDemo URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from app_demo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^hello/$', views.hello), # use url to find the def in views
    path('hrs/',include('hrs.urls')) , # use include to get all the path in one time
    path('polls/',include('polls.urls')), #include('polls.urls')) is the path like //djangoDemo/polls/urls.py
    path('vote/',include('schoolvoting.urls'))
]
