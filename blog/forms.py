from django.forms import ModelForm
from blog.models import Blog
from django import forms


class BlogForm(ModelForm):

    class Meta:
        model = Blog
        fields = ['title', 'body', 'image_preview', 'is_public', ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'image_preview': forms.FileInput(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox', }),
        }


class NoneForm(ModelForm):
    """Форма для отображения пустых значений для пользователей не являющихся content-manager"""
    class Meta:
        model = Blog
        fields = []