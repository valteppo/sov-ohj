from django import forms

from .models import Item, Comment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'price',
            'image',
        ]
        labels = {
            'name':'Nimi',
            'description':'Kuvaus',
            'price':'Hinta',
            'image':'Kuva'
        }
        widgets = {
            'description':forms.Textarea(attrs={'cols':80})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        labels = {
            'text':'Kommentti',
        }
        widgets = {
            'text':forms.Textarea(attrs={'cols':80})
        }
