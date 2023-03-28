from django import forms 
from .models import *
from ckeditor.fields import RichTextField

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author','category','body','image')
        
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'post title'}),
            'author': forms.TextInput(attrs= {'class': 'form-control', 'id':'author', 'value': '', 'type':'hidden'}),
            'category': forms.Select(attrs= {'class': 'form-control dropdown-toggle'}),
            'body': forms.Textarea(attrs= {'class': 'form-control', 'placeholder': 'post body'}),
        }
        
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body')
        
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'body': forms.Textarea(attrs= {'class': 'form-control'}),
        }
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control', 'placeholder': 'Category Title'}),
        }
        
