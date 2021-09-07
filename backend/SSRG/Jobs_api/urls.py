from django.urls import path
from .views import FailedJobList, JobList, JobDetail, PendingJobList, SuccessJobList

app_name = 'Jobs_api'

urlpatterns = [
    path('<int:pk>/', JobDetail.as_view(), name='createDetail'),
    path('', JobList.as_view(), name='createList'),
    path('jobstatus/failed', FailedJobList.as_view(), name = 'temp'),
    path('jobstatus/pending', PendingJobList.as_view(), name = 'temp1'),
    path('jobstatus/done', SuccessJobList.as_view(), name = 'temp2')
]