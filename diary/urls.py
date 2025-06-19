# diary/urls.py
from django.urls import path
from .views import DiaryListView, DiaryCreateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', DiaryListView.as_view(), name='diary_list'),
    path('create/', DiaryCreateView.as_view(), name='diary_create'),
    path('logout/', LogoutView.as_view(template_name='diary/logged_out.html'), name='logout'),  # ← ここが LogoutView の設定
]