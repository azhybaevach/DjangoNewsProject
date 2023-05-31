from django import forms
from .models import Comment, News


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'text', 'placeholder': 'Введите имя'}),
            'email': forms.EmailInput(attrs={'class': 'text', 'placeholder': 'Введите почту'}),
            'content': forms.Textarea(attrs={'class': 'text', 'placeholder': 'Введите текст'})
        }


class NewsForm(forms.ModelForm):
    image = forms.ImageField
    class Meta:
        model = News
        fields = ['title', 'description', 'image', 'category', 'owner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'text', 'placeholder': 'Тема'}),
            'owner': forms.TextInput(attrs={'class': 'text', 'placeholder': 'Автор поста'}),
            'description': forms.Textarea(attrs={'class': 'text', 'placeholder': 'Описание'}),
            'category': forms.Select(attrs={'class': 'text', 'placeholder': 'Категория'}),

        }


