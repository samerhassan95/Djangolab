from django.contrib import admin  
from django.urls import path  
from . import views 
urlpatterns = [ 
    path('liststudents',views.liststudents),
    path('liststaff',views.liststaff),
    path('mainreport',views.mainreport),
               ]