# coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from breastCancerApp.models import Subject, SubjectItem

def home(request):
    subjectList = Subject.objects.all()
    subject = subjectList.first()
    return render(request, 'home.html', {'subjectList': subjectList, 'subject': subject,})

def displaySubjectItems(request,subjectPrimaryKey):
    subjectList = Subject.objects.all()
    #subjectPrimaryKey = request.GET['pk']
    subject = subjectList.get(id=subjectPrimaryKey)

    subjectItemList=SubjectItem.objects.filter(foreign_Key=subjectPrimaryKey)
    return render(request, 'home.html', {'subject': subject, 'subjectList': subjectList,
                                         'subjectItemList': subjectItemList,})
