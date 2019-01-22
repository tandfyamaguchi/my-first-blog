from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        # Djangoにフォームを作るときのモデルを伝える
        model = Post
        # titleとtextのみフォームで使用 authorはログイン者,created_dateは日時が自動で設定
        fields = ('title', 'text',)
