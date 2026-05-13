from django import forms
from my_blog.models import Article

class PostForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "author",
            "category",
            "body"
        ]
        widgets = {
            'title': forms.TextInput(attrs = { 'class' : 'form-control' , 'placeholder':'Enter your title'}),
            'author': forms.Select(attrs = { 'class' : 'form-control' }),
            'category': forms.Select(attrs = { 'class' : 'form-control' , 'placeholder':'Please choose a category' }),
            'body': forms.Textarea(attrs = { 'class' : 'form-control' }),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            "title",
            "body"
        ]
        widgets = {
            'title': forms.TextInput(attrs = { 'class' : 'form-control' , 'placeholder':'Enter your title'}),
            'category': forms.Select(attrs = { 'class' : 'form-control' , 'placeholder':'Please choose a category' }),
            'body': forms.Textarea(attrs = { 'class' : 'form-control' }),
        }