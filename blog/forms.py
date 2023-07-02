from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    
    title = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter your title here',
        widget=forms.TextInput(
            attrs={
                'type':'text',
                'class':'form-control',
                'placeholder':'Your title goes here',
                'aria-label':'Title',
                'aria-describedby':'bascic-addon1',
                'title':'Your Blog title goes here',
                'id':'title-input'
            }
        )
    )
    
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'aria-label':'Content',
                'rows':'10',
                'title':'Your blog content goes here...'
            }
        ),
        required=True,
        
    )
    
    class Meta:
        model = Post
        exclude = [
            'author',
            'date_posted'
        ]