from django.db import models

class Diary(models.Model):
    title = models.CharField(
        max_length=100, 
        blank=False,
        verbose_name='タイトル',
        help_text='日記のタイトルを１００文字以内で入力してください'  # タイトル　空欄不可
        )
    content = models.TextField(
        verbose_name='本文',
        help_text='日記の内容を入力してください（長文可）',
        blank=False)              # 本文（長文可）　空欄不可 
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時　自動更新
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時　自動更新

    def __str__(self):
        return self.title
