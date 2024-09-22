from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.index,name='home'),
     path('mv_1/',views.mv_1,name='mv_1'),
    path('mv_2/',views.mv_2,name='mv_2'),
]