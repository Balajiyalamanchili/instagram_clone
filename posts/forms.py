from django import forms
from .models import Posts,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post_img', 'caption']



class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']