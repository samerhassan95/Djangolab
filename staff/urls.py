from django.contrib import admin  
from django.urls import path  
from . import views 
from django.urls import path
from .views import StaffListView, StaffInsertView, StaffUpdateView, StaffDeleteView
urlpatterns = [ 
    # path('list',views.list),
    # path('insert',views.insert),
    # path('update',views.update),
    # path('delete',views.delete),
    ##
    # path('', views.all_staff),
    # path('insert/', views.insert),
    # path('update/<int:sup_id>/', views.update, name="update_staff"),
    # path('delete/<int:sup_id>/', views.delete, name='delete_staff') 
        path('', StaffListView.as_view(), name='staff_list'),
    path('insert/', StaffInsertView.as_view(), name='staff_insert'),
    path('update/<int:sup_id>/', StaffUpdateView.as_view(), name='staff_update'),
    path('delete/<int:sup_id>/', StaffDeleteView.as_view(), name='staff_delete'),
                                ]