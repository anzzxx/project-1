from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    count=request.session.get('count',0)
    print(count)
    count=int(count)
    count=count+1
    request.session['count']=count
   
    response=render(request,'index.html',{'visits':count})
   
    return response
def mv_1(request):
    return render(request,'mv_1.html')
def mv_2(request):
    return render(request,'mv_2.html')
