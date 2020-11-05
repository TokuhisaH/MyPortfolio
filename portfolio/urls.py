#app

from django.conf.urls import url
from .views import homefunc,activityfunc,photographyfunc,contactfunc

urlpatterns = [
    url('activity/', activityfunc,name='activity'),
    url('photography/', photographyfunc,name='photography'),
    url('contact/', contactfunc,name='contact'),
    url('', homefunc,name='home'),
]
