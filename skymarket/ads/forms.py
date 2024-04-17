from django import forms

from ads.models import Ad


class AdForm(forms.ModelForm):
    """Форма для добавления продукта"""
    class Meta:
        model = Ad
        exclude = ('author',)