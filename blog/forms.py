from django import forms
from blog.models import Blog,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"