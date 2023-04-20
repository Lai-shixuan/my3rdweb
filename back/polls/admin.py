from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Question

admin.site.register(Question)   # 大概需要2个import去在admin中注册这个对象