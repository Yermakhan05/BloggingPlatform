from django import forms
from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Content', 'Author']
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the post title'}),
            'Content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
            'Author': forms.Select(attrs={'class': 'form-control-select'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['Author'].empty_label = "Select an author"


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['Title', 'Content']
        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the post title'}),
            'Content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['Content', 'Author']
        widgets = {
            'Author': forms.Select(attrs={'class': 'form-control'}),
            'Content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your content here...'}),
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['Author'].empty_label = "Select an author"
