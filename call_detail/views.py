#!/usr/bin/pythons
# -*- coding: utf-8
import MySQLdb
import re
from django.forms import modelformset_factory, modelform_factory
from django.shortcuts import render, render_to_response
import string
from .models import callDet
from django.http import HttpResponse
import json
import sqlparse
from django.template import loader
from .forms import FieldForm
from datetime import datetime, date, time
import sys
import json
from django.core.serializers.json import DjangoJSONEncoder

reload(sys)
sys.setdefaultencoding('utf8')


def index_view(request):



    if request.method == 'POST':
        rows  = request.POST.get('col_num', False)
        date_begin = request.POST.get('picker1',False)
        date_end = request.POST.get('picker2', False)
        source = request.POST.get('src', False)
        destination = request.POST.get('dst', False)
        answer = request.POST.get('ans', False)
        not_answer = request.POST.get('nans', False)
        busy = request.POST.get('busy',False)
        limit = request.POST.get('limit',False)
        print(limit)
        answer = int(answer)
        not_answer = int(not_answer)
        busy = int(busy)
        print(answer)
        print(not_answer)
        print(busy)
        message = str(unicode('Информация предоставлена за период с %s по %s' %(date_begin, date_end)))
        query = str('SELECT * FROM cdr where calldate>="%s" AND calldate<="%s"' %(date_begin,date_end))
        #fields = callDet.objects.raw(query)
        if source != "":
            src_query = str(" AND src = %d" %(int(source)))
            query = query + src_query

        if destination != "":
            dst_query = str(" AND dst = %d"%(int(destination)))
            query = query + dst_query

        if answer == 1 and not_answer == 0 and busy == 0:
            ans_query = str(' AND disposition = "ANSWERED"')
            query = query + ans_query
        elif answer == 1:
            ans_query = str(' AND (disposition = "ANSWERED"')
            query = query + ans_query

        if answer == 0 and not_answer == 1 and busy == 0:
            nans_query = str(' AND disposition = "NO ANSWER"')
            query = query + nans_query
        elif answer == 1 and not_answer == 1 and busy == 1:
            nans_query = str(' OR disposition = "NO ANSWER"')
            query = query + nans_query
        elif not_answer == 1 and answer == 0:
            nans_query = str(' AND (disposition = "NO ANSWER"')
            query = query + nans_query
        elif not_answer == 1 and answer == 1 and busy == 0:
            nans_query = str(' OR disposition =  "NO ANSWER"')
            query = query + nans_query
            query = query + ');'
        else:
            query = query

        if busy == 1 and answer == 0 and not_answer == 0:
            busy_query = str(' AND disposition =  "BUSY"')
            query = query + busy_query
        elif (busy ==1 and answer == 1) or (busy == 1 and not_answer == 1) or (busy ==1 and answer == 1 and not_answer == 1):
            busy_query = str(' OR disposition =  "BUSY"')
            query = query + busy_query
            query = query + ');'


        print(query)
        fields = callDet.objects.raw(query)
        ans_f = list(fields)
        print(type(ans_f))
        return render(request, 'detail/index.html', {'fields' : fields, 'message' : message})
    else:
        fields = callDet.objects.raw('SELECT * FROM cdr LIMIT 1;')
        print(type(fields))
        for p in fields:
            print(p.calldate)
            return render(request, 'detail/index.html', {'fields' : fields})
