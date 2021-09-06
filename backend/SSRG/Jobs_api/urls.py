from django.urls import path
from .views import JobList, JobDetail

app_name = 'Jobs_api'

urlpatterns = [
    path('<int:pk>/', JobDetail.as_view(), name='createDetail'),
    path('', JobList.as_view(), name='createList')
]