from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LANGUAGE_CHOICES, Jobs

class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class submitJob(forms.Form):
    language = forms.CharField(widget=forms.Select(choices=LANGUAGE_CHOICES), required=True)
    files = forms.FileField(required=True)
    baseFile = forms.CharField(required=False)