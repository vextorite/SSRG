from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import ClearableFileInput
from .models import LANGUAGE_CHOICES, Jobs, SingleFiles

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

class EditProfile(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username')

class SubmitJob(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ['slug', 'language','emailNow']
        labels = {'slug':'Job Name'}

class Files(forms.ModelForm):
    class Meta:
        model = SingleFiles
        fields = ['files', 'baseFile']
        widgets = {'files':ClearableFileInput(attrs={'multiple': True}), 
                    'baseFile':ClearableFileInput(attrs={'multiple':True})}
