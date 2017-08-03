"""official_demos URL Configuration

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
from demo1 import views as demo1_views

urlpatterns = [
    url(r'^articles/([0-9]{4})/$',demo1_views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$',demo1_views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]{2})/$',demo1_views.day_archive),
    url(r'^admin/', admin.site.urls),
]
