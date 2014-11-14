import os
import re
import shutil
import datetime
from django.contrib import admin
from django.conf import settings
from PictureInfo.models import *
# Register your models here.

def del_model(modeladmin, request, queryset):
    print '!!!!!!!!!'
    for obj in queryset:
        print obj.isrc.path
        if obj.isrc.path:
            os.remove(obj.isrc.path)
        obj.delete()
    modeladmin.message_user(request, 'Selected item(s) have been removed.')
del_model.short_description = 'Delete selected item(s)'

class PictureInfoAdmin(admin.ModelAdmin):
    list_display = ('pic_id', 'pic_name', 'time', 'type')
    list_filter = ('pic_id', 'pic_name', 'time')
    search_fields = ('pic_id', 'pic_name', 'time')
    actions = [del_model]

    def delete_model(self, request, obj):
        os.remove(obj.isrc.path)
        obj.delete()

    def save_model(self, request, obj, form, change):
        base_path = os.path.join(settings.BASE_DIR, 'upload')
        if change:
            change_list = form.changed_data
            init_data = form.initial
            print change_list
            if 'isrc' in change_list:
                os.remove(init_data['isrc'].path)
            #if ('type' in change_list) and ('isrc' not in change_list):
            #   date = datetime.date.strftime(init_data['time'], '%Y%m%d')
            #    change_path = os.path.join(os.path.abspath(base_path), form.data['type'], date)
            #    dir_list = os.listdir(os.path.join(os.path.abspath(base_path), form.data['type']))
            #    if date not in dir_list:
            #        update_path = os.path.join(os.path.join(os.path.abspath(base_path), form.data['type']), date)
            #        os.mkdir(update_path)
            #        img_path = os.path.join('./upload', form.data['type'], date)
                    #form.data['isrc']=
            #    shutil.move(init_data['isrc'].path, change_path)
        obj.save()

admin.site.register(PicInfo, PictureInfoAdmin)

class PicTypeAdmin(admin.ModelAdmin):
    list_display = ('typeid', 'type')

    def save_model(self, request, obj, form, change):
        base_path = os.path.join(settings.BASE_DIR, 'upload')
        dir_list = os.listdir(base_path)
        dir_exist = False
        for d in dir_list:
            if d == obj.typeid:
                dir_exist = True
                break
        if not dir_exist:
            os.mkdir(os.path.join(os.path.abspath(base_path), obj.typeid))
        obj.save()

admin.site.register(PicType, PicTypeAdmin)