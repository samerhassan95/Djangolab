from django.contrib import admin  
from django.urls import path  
from . import views 
urlpatterns = [ 
    # path('list',views.list),
    # path('insert',views.insert),
    # path('update',views.update),
    # path('delete',views.delete),
    ##
    path('', views.all_staff),
    path('insert/', views.insert),
    path('update/<int:sup_id>/', views.update, name="update_staff"),
    path('delete/<int:sup_id>/', views.delete, name='delete_staff') 
                                ]