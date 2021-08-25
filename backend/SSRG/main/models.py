from django.db import models

# Create your models here.

class Jobs(models.Model):
    #user = models.CharField(max_length=200)
    userEmail = models.EmailField(max_length=200)
    files = models.FileField(upload_to='jobs/')
    uploadDate = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50)
    baseFile = models.FileField(upload_to=...)

    def __str__(self):
        return self.userEmail+": "+str(self.uploadDate)

class User(models.Model):
    user = models.CharField(max_length=50)
    userEmail = models.EmailField(max_length=200)

    def __str__(self):
        return self.user