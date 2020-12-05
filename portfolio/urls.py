#app

from django.conf.urls import url,include
from django.contrib import admin
from .views import homefunc,activityfunc,photographyfunc,contactfunc,BlogList,BlogDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('activity/', activityfunc,name='activity'),
    url('photography/', photographyfunc,name='photography'),
    url('bloglist/',BlogList.as_view(), name='bloglist'),
    url('blogdetail/(?P<pk>\d+)',BlogDetail.as_view(),name='blogdetail'),
    url('contact/', contactfunc,name='contact'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#画像リンク指定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [url('', homefunc,name='home')]

