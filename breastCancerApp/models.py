# coding:utf-8
from django.db import models


class Subject(models.Model):
    subjectName = models.CharField(max_length=30, verbose_name="主题名称")
    subjectDescription = models.TextField(verbose_name="描述")
    subjectDisplaySequence = models.IntegerField(verbose_name="排序权重(数字)")

    def __str__(self):
        # 在Python3中使用 def __str__(self)
        return str(self.subjectDisplaySequence) + "." + self.subjectName


class SubjectItem(models.Model):
    subjectItemName = models.CharField(max_length=30, verbose_name="子标题名称")
    subjectItemDescription = models.TextField(verbose_name="描述", blank=True)
    subjectItemDetailDescription = models.TextField(verbose_name="详细描述", blank=True)
    foreign_Key = models.ForeignKey(Subject, verbose_name="外键")
    subjectItemDisplaySequence = models.IntegerField(verbose_name="排序权重(数字)")
    def __str__(self):
        # 在Python3中使用 def __str__(self)
        return str(self.subjectItemDisplaySequence) + "." + self.subjectItemName
