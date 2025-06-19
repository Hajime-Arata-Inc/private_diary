# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Diary
from django.views.generic import ListView


class DiaryCreateView(LoginRequiredMixin, CreateView):  # ← Mixinを追加　順番が重要
    model = Diary
    template_name = 'diary/diary_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('diary_list')

class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/diary_list.html'  # このテンプレートを後で作成します
    context_object_name = 'diary_list'       # テンプレートで使う変数名
    ordering = ['-created_at']               # 日付の新しい順で表示





    # CreateView はDjangoの汎用クラスビュー（Generic View）の1つ
    # model = Diary で対象モデルを指定
    # fields でフォームに表示するフィールドを指定
    # template_name で使うテンプレートを明示