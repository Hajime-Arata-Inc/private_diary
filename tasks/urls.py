from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='list'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/toggle/', views.toggle_done, name='toggle'),
]
