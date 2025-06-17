# Create your views here.
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Diary

class DiaryCreateView(CreateView):
    model = Diary
    fields = ['title', 'content']
    template_name = 'diary/diary_form.html'
    success_url = reverse_lazy('diary-list')

class DiaryListView(ListView):
    model = Diary
    template_name = 'diary/diary_list.html'

    # CreateView はDjangoの汎用クラスビュー（Generic View）の1つ
    # model = Diary で対象モデルを指定
    # fields でフォームに表示するフィールドを指定
    # template_name で使うテンプレートを明示