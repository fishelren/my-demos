from django.contrib import admin

# Register your models here.

from . import models # 从当前的包中导入models模块

admin.site.register([models.Reporter,models.Article])