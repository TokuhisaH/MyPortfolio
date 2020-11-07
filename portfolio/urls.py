#app

from django.conf.urls import url
from django.contrib import admin
from .views import homefunc,activityfunc,photographyfunc,contactfunc,BlogList,BlogDetail

urlpatterns = [
    url('activity/', activityfunc,name='activity'),
    url('photography/', photographyfunc,name='photography'),
    url('bloglist/',BlogList.as_view(), name='bloglist'),
    url('blogdetail/(?P<pk>\d+)',BlogDetail.as_view(),name='blogdetail'),
    url('contact/', contactfunc,name='contact'),
    url('', homefunc,name='home'),
]
