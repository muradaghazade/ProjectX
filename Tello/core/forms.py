from django import forms
from core.models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'author_surname','text']

        widgets = {
            'text': forms.Textarea(attrs={'id': 'question', 'placeholder': 'Rəyinizi buraya yazın', 'class': 'text-input-product'}),
            'author_name': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Adınızı daxil edin', 'class': 'input-product'}),
            'author_surname': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Soyadınızı daxil edin', 'class': 'input-product'})
        }