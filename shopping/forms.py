from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class meta:
        model = Post
        fields = ['title', 'desc', 'img', 'price']

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['img'].widget.attrs.update({'accept': 'image/*'})