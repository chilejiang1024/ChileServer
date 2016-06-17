#coding=utf-8

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><p>It is now %s.</p></body></html>" % now
    return HttpResponse(html)


def sort_gudou_gudou(request):
    html = "<html><body>"
    html += "</p>123<br>一二三"
    html += "</body></html>"
    return HttpResponse(html)


def get_index(request):
    return render(request, "index.html", locals())