from django import forms
from django.forms import Textarea

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ('text', )

        widgets = {
            'text': Textarea(attrs={
                'class': "form-control", 
                'placeholder': 'Comment',
                'style': 'max-width: 300px;',
                'id': 'formComment'
                })
        }