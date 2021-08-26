from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.
LANGUAGE_CHOICES = [('java', 'Java'), ('py', 'Python'), ('cpp', 'C++')]

class Jobs(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #userEmail = models.EmailField(max_length=200)
    files = models.FileField(upload_to='jobs/')
    uploadDate = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    baseFile = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username+"["+str(self.uploadDate)+"]"
