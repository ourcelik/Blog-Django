from django import forms
from django.db.models import fields
from .models import Comment


class CommentForm(forms.Form):
    name = forms.CharField(label='name', max_length=30,
                           widget=forms.TextInput(attrs={'class': 'f-name'}))
    comment = forms.CharField(
        label='comment', max_length=500, widget=forms.Textarea(attrs={'class': 'f-comment'}))
