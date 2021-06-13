from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .models import BlogModel,ActivityModel
import requests,json

def homefunc(request):
    return render(request, 'home.html',{})
    
def activityfunc(request):
    object_list = ActivityModel.objects.all()
    return render(request, 'activity.html',{'object_list':object_list})

class ActivityDetail(DetailView):
    template_name='activitydetail.html'
    model = ActivityModel
    
def photographyfunc(request):
    if request.method == 'GET':
        access_token='EAAL3zjlTZBiYBACnz5m4saeHvgxRrlAZAmRpWVhJvUAuZCQobf5PYOfd4fK2TggST5dl2jNTfnOIePT4CSczoAWfWcofSocpDHieRXwUXoZBZCSY8FdZAw9KWZAnDx8ZB885i7jOdUXZAotjOCO3teaC7WZAIrTltho9Cv23HmqoetkQZDZD'
        instagram_business_account="17841401949842264"
        count=60
        url = 'https://graph.facebook.com/v4.0/'+instagram_business_account+'?fields=media.limit('+str(count)+'){caption,media_url,permalink,timestamp,username}&access_token='+access_token
        r = requests.get(url)
        """
        result = []
        for x in r.json()['media']['data']:
            #print("x: ", x)
            result.append("media_url: ")
            #result.append(str(r.json()[x]['media_url']))
            result.append("permalink: ")
            #result.append(r.json()[x]['permalink'])
            result.append("timestanp: ")
            #result.append(r.json()[x]['timestamp'])
            result.append('\n')
    
            print(r.json()[x]['media_url'],
            "permalink: ", r.json()[x]['permalink'],
            "timestanp: ", r.json()[x]['timestamp'])
        
        mapped_num = map(str, result)
        result_string = ' '.join(mapped_num)
        print("result_string", result_string,)
        """
        
        return render(request, 'photography.html',{'result': r.json(),'count':count})
    else:
        return render(request, 'photography.html',{})

    return render(request, 'photography.html',{})
    
class BlogList(ListView):
    template_name = 'bloglist.html'
    model = BlogModel
    def get_queryset(self):
        # 公開フラグがTrueで、作成日順に並び替え
        return super().get_queryset().order_by('-date')
    
class BlogDetail(DetailView):
    template_name='blogdetail.html'
    model = BlogModel
        
def contactfunc(request):
    return render(request, 'contact.html',{})