# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Diary
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.db.models import Count
from django.db.models.functions import TruncDate


class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/diary_list.html'
    context_object_name = 'diary_list'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diary_count'] = Diary.objects.count()

        # 🔽 日別件数を集計（TruncDateで日付単位に切り落とし）
        context['daily_counts'] = (
            Diary.objects
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('-date')
        )

        return context


class DiaryCreateView(LoginRequiredMixin, CreateView):  # ← Mixinを追加　順番が重要
    model = Diary
    template_name = 'diary/diary_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('diary_list')


class UserLoginView(LoginView):
    template_name = 'diary/login.html'

class UserLogoutView(LogoutView):
    template_name = 'diary/logged_out.html'  # ログアウト後に表示するテンプレート



    # CreateView はDjangoの汎用クラスビュー（Generic View）の1つ
    # model = Diary で対象モデルを指定
    # fields でフォームに表示するフィールドを指定
    # template_name で使うテンプレートを明示