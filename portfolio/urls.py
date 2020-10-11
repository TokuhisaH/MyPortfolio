#app

from django.conf.urls import url
from .views import homefunc,profilefunc

urlpatterns = [
    url('profile/', profilefunc,name='profile'),
    url('', homefunc,name='home'),
]
