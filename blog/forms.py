from __future__ import unicode_literals
from django import forms
from .models import Article, Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('commenter', 'content',)