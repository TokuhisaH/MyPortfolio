#app

from django.conf.urls import url
from .views import homefunc,profilefunc

urlpatterns = [
    url('home/', homefunc,name='home'),
    url('profile/', profilefunc,name='profile'),
]
