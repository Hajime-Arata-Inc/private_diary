# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import UpdateView, DeleteView
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Diary







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

#【メモ】現在 DiaryListView に統計処理も含まれているが、分析画面（stats.html）を独立させる際に StatsView に分離予定。

    def get_queryset(self):
        # 自分が投稿した日記だけを取得
        return Diary.objects.filter(user=self.request.user)

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
    fields = ['title', 'content']
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class UserLoginView(LoginView):
    template_name = 'diary/login.html'

class UserLogoutView(LogoutView):
    template_name = 'diary/logged_out.html'  # ログアウト後に表示するテンプレート


class DiaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Diary
    fields = ['title', 'content']
    template_name = 'diary/diary_form.html'  # 投稿と同じテンプレートを再利用
    success_url = reverse_lazy('diary_list')

    def test_func(self):
        return self.get_object().user == self.request.user  # 投稿者のみ編集OK


class DiaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Diary
    template_name = 'diary/diary_confirm_delete.html'
    success_url = reverse_lazy('diary_list')

    def test_func(self):
        return self.get_object().user == self.request.user  # 投稿者のみ削除OK

    # CreateView はDjangoの汎用クラスビュー（Generic View）の1つ
    # model = Diary で対象モデルを指定
    # fields でフォームに表示するフィールドを指定
    # template_name で使うテンプレートを明示

class UserLoginView(LoginView):
    template_name = 'diary/login.html'
    redirect_authenticated_user = True

class SignUpView(CreateView):
    template_name = 'diary/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # 登録成功後にログイン画面へリダイレクト