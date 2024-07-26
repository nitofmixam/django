from django.forms import ModelForm
from .models import Product, Version, Category
from django import forms


class ProductForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_preview', 'category', 'price', 'public', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_preview': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox', }),
        }

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        name = self.cleaned_data['name']
        print(self.cleaned_data)
        if name.lower() in forbidden_words:
            raise forms.ValidationError("Название товара не может включать запрещенные слова")
        return self.cleaned_data['name']


class ProductModeratorUpdateForm(ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')
    class Meta:
        model = Product
        fields = ['name', 'description', 'image_preview', 'category', 'price', 'public', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image_preview': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'public': forms.CheckboxInput(attrs={'type': 'checkbox', 'class': 'checkbox', }),
        }

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        name = self.cleaned_data['name']
        print(self.cleaned_data)
        if name.lower() in forbidden_words:
            raise forms.ValidationError("Название товара не может включать запрещенные слова")
        return self.cleaned_data['name']


class ProductUserUpdateForm(ModelForm):

    class Meta:
        model = Product
        fields = []


class VersionForm(ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        widgets = {
            'version_number': forms.TextInput(attrs={'class': 'form-control'}),
            'version_name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'version_number': 'Номер версии',
            'version_name': 'Название версии',
            'is_active': 'Активная версия',
        }