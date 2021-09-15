<<<<<<< HEAD
#from Jobs.views import singleJobDetail
=======
#from backend.SSRG.Jobs.views import singleJobDetail
>>>>>>> 8584af2d1f68e629b177520183cb9174fade3203
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
LANGUAGE_CHOICES = [('.java', 'Java'), ('.py', 'Python'), ('.cpp', 'C++'),
                    ('.c', 'C'), ('.cs', 'C#'), ('.vb', 'Visual Basic'), ('.js', 'Javascript'),
                    ('.f90', 'FORTRAN'), ('.ml', 'ML'), ('.hs', 'Haskell'), ('.lsp','Lisp'), ('.scm', 'Scheme'), 
                    ('.pas', 'Pascal'), ('.m2', 'Modula2'), ('.ada', 'Ada'), ('.pl', 'Perl'), ('.tcl', 'TCL'), ('.m', 'Matlab'), 
                    ('.vhd', 'VHDL'), ('.v', 'Verilog'), ('.asc', 'Spice'), ('.asm', 'MIPS assembly'), ('.asm', 'a8086 assembly'), 
                    ('.hcl', 'HCL2')]
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
    jobState = models.CharField(max_length=100, choices=STATE_OPTIONS, default='processing')
    slug = models.SlugField(max_length=200, unique_for_date='uploadDate')
    objects = models.Manager()
    failedJobObjects = FailedJobObjects()
    pendingJobObjects = PendingJobObjects()
    successJobObjects = SuccessJobObjects()

    def __str__(self):
        return self.user.username+"["+str(self.uploadDate)+"]"

<<<<<<< HEAD
    def get_absolute_url(self):
        return reverse('singleJobDetail', args=[self.slug])
=======
 #   def get_absolute_url(self):
    #    return reverse(singleJobDetail, args=[self.slug])
>>>>>>> 8584af2d1f68e629b177520183cb9174fade3203

    class Meta:
        ordering = ('-uploadDate',)