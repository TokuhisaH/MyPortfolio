from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import BlogModel


def homefunc(request):
    return render(request, 'home.html',{})
    
def activityfunc(request):
    return render(request, 'activity.html',{})
    
def photographyfunc(request):
    return render(request, 'photography.html',{})
    
class BlogList(ListView):
    template_name = 'bloglist.html'
    model = BlogModel

class BlogDetail(DetailView):
    template_name='blogdetail.html'
    model = BlogModel
        
def contactfunc(request):
    return render(request, 'contact.html',{})