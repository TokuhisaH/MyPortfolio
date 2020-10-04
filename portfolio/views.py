from django.shortcuts import render,redirect

def homefunc(request):
    return render(request, 'home.html',{})
    
def profilefunc(request):
    return render(request, 'profile.html',{})