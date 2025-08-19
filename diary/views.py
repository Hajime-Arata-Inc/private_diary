from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models.functions import TruncDate
from django.db.models import Count
from django.urls import reverse_lazy
from .models import Diary


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

    def get_queryset(self):
        # 自分が投稿した日記だけ
        return Diary.objects.filter(user=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 自分の投稿数に限定
        context['diary_count'] = Diary.objects.filter(user=self.request.user).count()
        # （必要なら）自分の投稿のみ日次集計
        context['daily_counts'] = (
            Diary.objects.filter(user=self.request.user)
            .annotate(date=TruncDate('created_at'))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('-date')
        )
        return context


class DiaryCreateView(LoginRequiredMixin, CreateView):
    model = Diary
    fields = ['title', 'content']
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
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
