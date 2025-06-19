# diary/urls.py
from django.urls import path
from .views import DiaryListView, DiaryCreateView

urlpatterns = [
    path('', DiaryListView.as_view(), name='diary_list'),
    path('create/', DiaryCreateView.as_view(), name='diary-create'),
]

