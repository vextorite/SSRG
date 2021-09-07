from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
LANGUAGE_CHOICES = [('java', 'Java'), ('py', 'Python'), ('cpp', 'C++')] #other options later
STATE_OPTIONS = [('done', 'Done'), ('processing', 'Processing'), ('error', 'Error')]
EMAIL_OPTIONS = [('True', 'True'), ('False', 'False')]

class Jobs(models.Model):

    class FailedJobObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(jobState='error')

    class PendingJobObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(jobState='processing')

    class SuccessJobObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(jobState='done')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    files = models.FileField(upload_to='jobs/')
    uploadDate = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    baseFile = models.CharField(max_length=200)
    emailNow = models.CharField(max_length=10, choices=EMAIL_OPTIONS)
    jobState = models.CharField(max_length=100, choices=STATE_OPTIONS)
    jobRef = str(uploadDate)
    objects = models.Manager()
    failedJobObjects = FailedJobObjects()
    pendingJobObjects = PendingJobObjects()
    successJobObjects = SuccessJobObjects()

    def __str__(self):
        return self.user.username+"["+str(self.uploadDate)+"]"