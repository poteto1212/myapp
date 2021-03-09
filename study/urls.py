from django.urls import path
from .import views

app_name='studys'
urlpatterns=[
    path('',views.index,name='index'),
    path('studya',views.studya,name='studya'),
    path('studyb',views.studyb,name='studyb'),
    path('paizas',views.paizas,name='paizas'),
    path('paizaa',views.paizaa,name='paizaa'),
    path('paizab',views.paizab,name='paizab'),
    path('myinfo',views.myinfo,name='myinfo')
    ]