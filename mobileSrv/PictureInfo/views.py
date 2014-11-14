from datetime import datetime, date, timedelta
import json
from django.contrib.sessions.models import Session
from urlparse import urlparse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings
from django.db.models import Q
from PictureInfo.models import PicInfo

# Create your views here.

def get_pic(request):
    timeoffset = 0
    if not isinstance(request, HttpRequest):
        raise
    if request.method == 'POST':
        data = json.loads(request.body)
    else:
        if request.GET.get('dateindex'):
            timeoffset = request.GET.get('dateindex')
        endtime = request.GET.get('date')
        type = str(request.GET.get('type')).split(',')
        if request.GET.get('basetime'):
            basetime = datetime.strptime(request.GET.get('basetime'), '%Y-%m-%d')
        if request.GET.get('type') is None:
            return HttpResponse(json.dumps({'error': 'ERROR_TYPE', 'success': False}))
    pic_list = []
    today = datetime.now()
    datelist = []
    timelist = PicInfo.objects.filter().values('time').distinct().order_by('-time')
    for t in timelist:
        tmp = datetime.strptime(datetime.strftime(t['time'], '%Y-%m-%d'), '%Y-%m-%d')
        datelist.append(tmp)
    #datelist = [t['time'] for t in timelist]
    try:
        index = datelist.index(basetime)
        time_list = [t['time'] for t in timelist[index:]]
    except:
        return HttpResponse(json.dumps({'error': 'BASETIME NOT EXIST', 'success': False}))
    try:
        t = int(timeoffset)
    except:
        return HttpResponse(json.dumps({'error': 'WRONG_PARAM:dataindex', 'success': False}))
    #deltatime = timedelta(days=0 - t)
    #time = today + deltatime
    final = False
    if t >= len(time_list) - 1:
        time = time_list[-1]
        final = True
    else:
        time = time_list[t]
    time = datetime.strftime(time, "%Y-%m-%d")
    if time is not None:
        stime = datetime.strptime(time, "%Y-%m-%d")
        pics = PicInfo.objects.filter(Q(type__typeid__in=type) & Q(time=stime))
    else:
        pics = PicInfo.objects.filter(type__typeid__in=type)
    pic_count = len(pics)
    for p in pics:
        pic_list.append({
            'photo_id': p.pic_id,
            'photo_name': p.pic_name,
            'iwd': p.iwd,
            'iht': p.iht,
            'isrc': settings.PICTURT_DOWNLOAD_BASE_URL + p.isrc.path,
            'uploadtime': date.strftime(p.time, '%Y%m%d'),
            'msg': p.msg,
        })
    data = {
        'picsize': pic_count,
        'pic': pic_list,
    }
    return HttpResponse(json.dumps({'data': data, 'final': final,'success': True}))

def get_basetime(request):
    if not isinstance(request, HttpRequest):
        raise
    if request.method == 'POST':
        data = json.loads(request.body)
    else:
        timelist = PicInfo.objects.filter().values('time').distinct().order_by('time')
    lastdate = []
    if len(timelist) > 0:
        lastdate = [t['time'] for t in timelist]
    #return HttpResponse(json.dumps({'basetime': datetime.strftime(lastdate[0], '%Y%m%d'), 'success': True}))
    return HttpResponse(datetime.strftime(lastdate[0], '%Y-%m-%d'))



