from django import forms

from .models import Item, Comment

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'price'
        ]
        labels = {
            'name':'Nimi',
            'description':'Kuvaus',
            'price':'hinta',
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
