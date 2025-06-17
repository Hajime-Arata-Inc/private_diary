from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=100)  # タイトル（１００文字）
    content = models.TextField()              # 本文（長文可）
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時　自動更新
    updated_at = models.DateTimeField(auto_now=True)      # 更新日時　自動更新

    def __str__(self):
        return self.title
