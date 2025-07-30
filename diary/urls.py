# diary/urls.py
from django.urls import path
from .views import DiaryListView, DiaryCreateView
from .views import UserLoginView  # ✅ ここが必要！
from .views import UserLogoutView  # ✅ 自作ビューを読み込む
from .views import StatsView
from .views import DiaryUpdateView, DiaryDeleteView
from .views import SignUpView  # ← 追加



urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('', DiaryListView.as_view(), name='diary_list'),
    path('create/', DiaryCreateView.as_view(), name='diary_create'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('diary/<int:pk>/update/', DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>/delete/', DiaryDeleteView.as_view(), name='diary_delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
]



