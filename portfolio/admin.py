from django.contrib import admin
from .models import BlogModel,ActivityModel
# Register your models here.

#管理画面でモデルを操作できるように設定する
admin.site.register(BlogModel)

admin.site.register(ActivityModel)
# Register your models here.
