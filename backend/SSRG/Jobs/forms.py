from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class MetaData:
        model = User
        fields = ("username", "email", "password", "passwordConf")

    def save(self, commit=True):
        user = super(NewUser, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
