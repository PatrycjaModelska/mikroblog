from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ("post", "created", "update", "active")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'short', 'contents', 'category')

        widgets = {
            'title': forms.Textarea(attrs={'class': 'input', 'cols': 100, 'rows': 1, 'placeholder': 'Dodaj tytuł'}),
            'short': forms.Textarea(attrs={'class': 'input', 'cols': 100, 'rows': 5,
                                           'placeholder': 'Wprowadź zapowiedź, którą wyświetlimy na stronie głównej.'}),
        }

    category = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        required=False,
        queryset=BlogCategory.objects.all()
    )
