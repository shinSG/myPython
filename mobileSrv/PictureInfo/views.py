import datetime
import json
from urlparse import urlparse
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.conf import settings
from django.db.models import Q
from PictureInfo.models import PicInfo

# Create your views here.

def get_pic(request):
    if not isinstance(request, HttpRequest):
        raise
    if request.method == 'POST':
        data = json.loads(request.body)
    else:
        starttime = request.GET.get('date')
        print starttime
        endtime = request.GET.get('date')
        print endtime
        type = str(request.GET.get('type')).split(',')
        print type
    pic_list = []
    if starttime is not None:
        stime = datetime.datetime.strptime(starttime, "%Y-%m-%d")
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
            'msg': p.msg,
        })
    data = {
        'picsize': pic_count,
        'pic': pic_list,
    }
    return HttpResponse(json.dumps({'data': data, 'success': True}))



