from django.contrib import admin
from .models import BlogModel,ActivityModel
from adminsortable.admin import SortableAdmin
# Register your models here.

#管理画面でモデルを操作できるように設定する
admin.site.register(BlogModel)

# SortableAdminを継承
class ActivityModelAdmin(SortableAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(ActivityModel,ActivityModelAdmin)
# Register your models here.
