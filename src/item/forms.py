from django import forms
from .models import Item

INPUT_CLASSE = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
            'class' : INPUT_CLASSE
            }),
            'name': forms.TextInput(attrs={
            'class' : INPUT_CLASSE
            }),
            'description': forms.Textarea(attrs={
            'class' : INPUT_CLASSE
            }),
            'price': forms.TextInput(attrs={
            'class' : INPUT_CLASSE
            }),
            'image': forms.FileInput(attrs={
            'class' : INPUT_CLASSE
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
            'class' : INPUT_CLASSE
            }),
            'description': forms.Textarea(attrs={
            'class' : INPUT_CLASSE
            }),
            'price': forms.TextInput(attrs={
            'class' : INPUT_CLASSE
            }),
            'image': forms.FileInput(attrs={
            'class' : INPUT_CLASSE
            }),
        }
