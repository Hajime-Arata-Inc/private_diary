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
from django.views.generic import TemplateView
from django.contrib.auth.mixins import UserPassesTestMixin

class StatsView(LoginRequiredMixin, TemplateView, UserPassesTestMixin):
    template_name = 'diary/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        daily_counts = (
            Diary.objects
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('-date')
        )

        # グラフ用データ
        context['daily_counts'] = daily_counts
        context['diary_count'] = Diary.objects.count()
        # ここでNoneが入らないように安全に変換
        context['dates'] = [
            item['date'].strftime('%Y-%m-%d') if item['date'] else '不明'
            for item in daily_counts
        ]
        context['counts'] = [item['count'] for item in daily_counts]

        return context

    def test_func(self):
        return self.request.user.is_staff  # ✅ スタッフユーザーのみ許可

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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'diary/login.html'

class UserLogoutView(LogoutView):
    template_name = 'diary/logged_out.html'  # ログアウト後に表示するテンプレート



    # CreateView はDjangoの汎用クラスビュー（Generic View）の1つ
    # model = Diary で対象モデルを指定
    # fields でフォームに表示するフィールドを指定
    # template_name で使うテンプレートを明示