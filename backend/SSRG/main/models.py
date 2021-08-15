from django.db import models

# Create your models here.

class Jobs(models.Model):
    user = models.CharField(max_length=200)
    userEmail = models.EmailField(max_length=200)
    files = models.FileField(upload_to='jobs/')
    uploadDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user+": "+str(self.uploadDate)