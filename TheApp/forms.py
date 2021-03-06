from django import forms
from django.contrib.auth.models import User
from TheApp.models import UserProfileInfo, Post, Comment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class PostForm(forms.ModelForm):

    class Meta():
        model = Post

        fields = ('title', 'text')



class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('text',)
