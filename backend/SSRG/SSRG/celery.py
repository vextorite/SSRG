from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SSRG.settings') #setting default settings in Django for the celery program
app = Celery('SSRG')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def testTask(self, filename, username, slug, language, basefile, email, emailNow, path):
    os.system(
    f"python3 {filename} {username} {slug} {language} 'False' '' {basefile} {email} {path}")
    #print(slug+"\n"+path)