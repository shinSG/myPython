import os
from django.contrib import admin
from django.conf import settings
from PictureInfo.models import *
# Register your models here.

def del_model(modeladmin, request, queryset):
    print '!!!!!!!!!'
    for obj in queryset:
        print obj.isrc.path
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
        print '!!!!!!!!!'
        os.remove(obj.isrc.path)
        obj.delete()


admin.site.register(PicInfo, PictureInfoAdmin)

class PicTypeAdmin(admin.ModelAdmin):
    list_display = ('typeid', 'type')

    def save_model(self, request, obj, form, change):
        base_path = os.path.join(settings.BASE_DIR, 'upload')
        print settings.BASE_DIR
        print base_path
        dir_list = os.listdir(base_path)
        dir_exist = False
        for d in dir_list:
            if d == obj.typeid:
                dir_exist = True
                break
        print os.path.join(os.path.abspath(base_path), obj.typeid)
        if not dir_exist:
            os.mkdir(os.path.join(os.path.abspath(base_path), obj.typeid))
        obj.save()

admin.site.register(PicType, PicTypeAdmin)