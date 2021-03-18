from django import forms
from .models import Blog

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','content' ,'author', 'image']