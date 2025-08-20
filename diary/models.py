from django.db import models
from django.contrib.auth.models import User  # ユーザーモデルのインポート

from django.contrib.auth.models import User

class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 🔴 追加！
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
