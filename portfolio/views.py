from django.shortcuts import render,redirect

def homefunc(request):
    return render(request, 'home.html',{})
    
def activityfunc(request):
    return render(request, 'activity.html',{})
    
def photographyfunc(request):
    return render(request, 'photography.html',{})
        
def contactfunc(request):
    return render(request, 'contact.html',{})