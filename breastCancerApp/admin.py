# coding:utf-8
from django.contrib import admin

# Register your models here.
from breastCancerApp.models import SubjectItem, Subject

admin.site.register(Subject)
admin.site.register(SubjectItem)
