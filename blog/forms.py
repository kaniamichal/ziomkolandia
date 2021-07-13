from captcha.fields import CaptchaField
from django.forms import ModelForm

from .models import Comment, ReplyComment


class CommentPost(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']


class ReplayCommentForm(ModelForm):
    class Meta:
        model = ReplyComment
        fields = ['replay_name', 'replay_content']
