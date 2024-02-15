from django import forms

class PostForm(forms.Form):
    photo = forms.ImageField()
    notes = forms.CharField(max_length=200)