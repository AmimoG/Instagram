from django import forms
from .models import Profile, Image
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class PostForm(forms.ModelForm):
  class Meta:
    model = Image
    fields = ('image_caption', 'image', 'tag_someone',)

class SignUpForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['bio','profile_pic','profile_avatar','date']