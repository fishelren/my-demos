"""KeyPointsSummary URL Configuration

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
from demo import views as demo_views
urlpatterns = [
    url(r'^$',demo_views.sayHello),
    url(r'^add$',demo_views.add),
    url(r'^msg/',demo_views.msg),
    url(r'^template1/',demo_views.template1),
    url(r'^template2/',demo_views.template2),
    url(r'^template3/',demo_views.template3),
    url(r'^template4/',demo_views.template4),
    url(r'^create/',demo_views.create),
    url(r'^delete/',demo_views.delete),
    url(r'^update/',demo_views.update),
    url(r'^research/',demo_views.research),
    url(r'^form1/',demo_views.form1),
    url(r'^info/',demo_views.getInfo),
    url(r'^index/',demo_views.index),
    url(r'^admin/', admin.site.urls),]
