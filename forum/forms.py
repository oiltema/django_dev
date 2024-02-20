from django import forms
from django.contrib.auth import get_user_model

from forum.models import Post, Comments


class AddNewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'status', 'slug', 'categories']

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Nick name')
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput())

class AddCommentForm(forms.ModelForm):
    comment = forms.CharField(label='Comment')
    class Meta:
        model = Comments
        fields = ['comment']

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Nick name',
                               widget=forms.TextInput())
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput())
    password2 = forms.CharField(label='Again Password',
                               widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        # fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password2']
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Different pass")
        return cd['password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username = username).exists():
            raise forms.ValidationError('This username already exist!')
        return username