# diary/urls.py

# diary/urls.py
from django.urls import path
from .views import (
    DiaryListView, DiaryCreateView, DiaryUpdateView, DiaryDeleteView,
    StatsView, SignUpView,
)

app_name = 'diary'  # ← 必須（namespaced URL で逆引き安定）

urlpatterns = [
    path('', DiaryListView.as_view(), name='list'),
    path('create/', DiaryCreateView.as_view(), name='create'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('<int:pk>/update/', DiaryUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', DiaryDeleteView.as_view(), name='delete'),

    # サインアップ（自作ビューはOK）
    path('signup/', SignUpView.as_view(), name='signup'),
]
