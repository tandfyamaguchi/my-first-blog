from django.db import models
from django.utils import timezone


class Post(models.Model):
    # 他のモデルへのリンク
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # 文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    # 制限無しの長いテキスト用
    text = models.TextField()
    # 日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
