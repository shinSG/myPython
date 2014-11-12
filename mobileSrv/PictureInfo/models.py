import os
import datetime
from django.db import models
from django.conf import settings
# Create your models here.
class PicType(models.Model):
    typeid = models.CharField(max_length=64, primary_key=True)
    type = models.CharField(max_length=128)

    def __unicode__(self):
        return self.type


def get_upload_path(instance, filename):
    dir_path = os.path.join(settings.PICTURT_UPLOAD_DIR, instance.type.typeid)
    today_str = datetime.date.strftime(datetime.date.today(), '%Y%m%d')
    dir_list = os.listdir(dir_path)
    dir_exist = False
    for d in dir_list:
        if d == today_str:
            dir_exist = True
            break
    if not dir_exist:
        os.mkdir(os.path.join(os.path.abspath(dir_path), today_str))
    return os.path.join(settings.PICTURT_UPLOAD_DIR, instance.type.typeid + '/' + today_str + '/' + filename)

class PicInfo(models.Model):
    pic_id = models.CharField(max_length=128, primary_key=True, unique=True)
    pic_name = models.CharField(max_length=256)
    iwd = models.IntegerField(max_length=20, default=0)
    iht = models.IntegerField(max_length=20, default=0)
    msg = models.TextField(blank=True)
    time = models.DateField(default=datetime.date.today())
    type = models.ForeignKey(PicType)
    isrc = models.ImageField(upload_to=get_upload_path)


    def __unicode__(self):
        return self.pic_name
    #object = PhotoManager()



#class PhotoManager(models.Manager):