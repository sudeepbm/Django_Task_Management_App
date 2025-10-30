from django.urls import path
from base import views

urlpatterns = [
    # Add your app's URL patterns here
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('completed/', views.completed, name='completed'),
    path('mark_complete/<int:pk>/', views.mark_complete, name='mark_complete'),
    path('mark_incomplete/<int:pk>/', views.mark_incomplete, name='mark_incomplete'),
    path('history/', views.history, name='history'),
    path('delete_all_history/', views.delete_all_history, name='delete_all_history'),
    path('restore_all_tasks/', views.restore_all_tasks, name='restore_all_tasks'),
    path('delete_history/<int:pk>/', views.delete_history, name='delete_history'),
    path('restore_task/<int:pk>/', views.restore_task, name='restore_task'),
    path('about/', views.about, name='about'),
    path('support/', views.support, name='support'),
]
