from django.contrib import admin  
from django.urls import path  
from . import views 
# urlpatterns = [ 
#     path('list',views.list),
#     path('insert',views.insert),
#     path('update',views.update),
#     path('delete',views.delete),
#     ##
#     path('', views.student_list, name='student_list'),
#     path('<int:id>/', views.student_detail, name='student_detail'),
#     path('new/', views.student_create, name='student_create'),
#     path('<int:id>/edit/', views.student_update, name='student_update'),
#     path('<int:id>/delete/', views.student_delete, name='student_delete'),
#                ]
urlpatterns = [
    path('', views.all_std, name="all_std"),
    path('insert/', views.insert),
    path('update/<int:std_id>/', views.update, name='update_student'),
    path('delete/<int:std_id>/', views.delete, name='delete_student')
]