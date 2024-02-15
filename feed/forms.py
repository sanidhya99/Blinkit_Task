from django import forms

class PostForm(forms.Form):
    photo = forms.ImageField(label_suffix='', widget=forms.ClearableFileInput(attrs={'id': 'photo_input','placeholder': 'Click here'}))
    notes = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Enter your notes here...'}))