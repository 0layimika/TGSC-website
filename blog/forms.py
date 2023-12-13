from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['opinion']
        widgets = {
            'opinion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Your comment here'}),
        }
