#!/usr/bin/python
# -*- coding: utf-8
from django.db import models
import MySQLdb
import string

# Create your models here.
#db = MySQLdb.connect(host="194.54.64.40", user="eugen", passwd="eugen", db="asterisk", charset='utf8')
#query = "SELECT calldate, src, dst, billsec, disposition  FROM cdr LIMIT 10"
class callDet(models.Model):
    calldate = models.DateTimeField(verbose_name="Дата звонка", )
    src = models.TextField(verbose_name="Номер источника")
    dst = models.TextField(verbose_name="Номер назначения")
    billsec = models.CharField(verbose_name="Время звонка", max_length = 20)
    disposition = models.CharField (verbose_name="Статус звонка", max_length = 20)
