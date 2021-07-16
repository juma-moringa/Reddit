from redditclone.models import Post
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class  RedditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','url']