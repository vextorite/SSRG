from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
LANGUAGE_CHOICES = [('java', 'Java'), ('py', 'Python'), ('cpp', 'C++'),('c', 'C'), 
                    ('cs', 'C#'), ('vb', 'Visual Basic'), ('js', 'Javascript'),('f90', 'FORTRAN'), 
                    ('ml', 'ML'), ('hs', 'Haskell'), ('lsp','Lisp'), ('scm', 'Scheme'), ('pas', 'Pascal'), 
                    ('m2', 'Modula2'), ('ada', 'Ada'), ('pl', 'Perl'), ('tcl', 'TCL'), ('m', 'Matlab'), ('vhd', 'VHDL'), 
                    ('v', 'Verilog'), ('asc', 'Spice'), ('asm', 'MIPS assembly'), ('asm', 'a8086 assembly'), ('hcl', 'HCL2')]
STATE_OPTIONS = [('done', 'Done'), ('processing', 'Processing'), ('error', 'Error')]
EMAIL_OPTIONS = [('True', 'True'), ('False', 'False')]

def get_upload_path(instance, filename):
    return 'jobs/{0}/{1}/Zip/{2}'.format(instance.user.username, instance.slug, filename)

def get_base_path(instance, filename):
    return 'jobs/{0}/{1}/Basefiles/{2}'.format(instance.user.username, instance.slug, filename)

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
    uploadDate = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    emailNow = models.CharField(max_length=10, choices=EMAIL_OPTIONS)
    jobState = models.CharField(max_length=100, choices=STATE_OPTIONS, default='processing')
    slug = models.SlugField(max_length=200)
    objects = models.Manager()
    failedJobObjects = FailedJobObjects()
    pendingJobObjects = PendingJobObjects()
    successJobObjects = SuccessJobObjects()

    def __str__(self):
        return self.user.username+": "+str(self.slug)

    def get_absolute_url(self):
        return reverse('singleJobDetail', args=[self.slug])


    class Meta:
        ordering = ('-uploadDate',)

class SingleFiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200)
    files = models.FileField(upload_to=get_upload_path, blank=True, null=True)
    baseFile = models.FileField(upload_to=get_base_path, blank=True, null=True)
    jobInstance = models.ForeignKey(Jobs, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username+": "+str(self.slug)+": "+str(self.files)
