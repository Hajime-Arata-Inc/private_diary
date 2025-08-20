from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.db.models.functions import TruncDate
from django.db.models import Count
from .models import Diary
from django.contrib import messages





class StatsView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'diary/stats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 自分の投稿のみ日次集計
        daily_counts = (
            Diary.objects.filter(user=self.request.user)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('-date')
        )

        context['daily_counts'] = daily_counts
        context['diary_count'] = Diary.objects.filter(user=self.request.user).count()
        context['dates'] = [
            item['date'].strftime('%Y-%m-%d') if item['date'] else '不明'
            for item in daily_counts
        ]
        context['counts'] = [item['count'] for item in daily_counts]
        return context

    def test_func(self):
        # スタッフのみアクセス許可（要件に応じて変更可）
        return self.request.user.is_staff


class DiaryListView(LoginRequiredMixin, ListView):
    model = Diary
    template_name = 'diary/diary_list.html'
    context_object_name = 'diary_list'
    ordering = ['-created_at']
    paginate_by = 10    

    def get_queryset(self):
        # 自分が投稿した日記だけ
        return Diary.objects.filter(user=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        qs = Diary.objects.filter(user=self.request.user)
        context['diary_count'] = qs.count()
        context['daily_counts'] = (
            qs.annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('-date')
        )
        # グラフ用（必要なければ省略可）
        context['dates']  = [d['date'].strftime('%Y-%m-%d') for d in context['daily_counts']]
        context['counts'] = [d['count'] for d in context['daily_counts']]
        return context


class DiaryCreateView(LoginRequiredMixin, CreateView):
    model = Diary
    fields = ['title', 'content']
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        # 例: CreateViewのform_valid内で
        messages.success(self.request, "保存しました")
        return super().form_valid(form)


class DiaryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Diary
    fields = ['title', 'content']
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    def test_func(self):
        return self.get_object().user == self.request.user


class DiaryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Diary
    template_name = 'diary/diary_confirm_delete.html'
    success_url = reverse_lazy('diary:list')

    def test_func(self):
        return self.get_object().user == self.request.user


class SignUpView(CreateView):
    template_name = 'diary/signup.html'
    form_class = UserCreationForm
    # 標準認証（/accounts/login/）にリダイレクト
    success_url = reverse_lazy('login')

