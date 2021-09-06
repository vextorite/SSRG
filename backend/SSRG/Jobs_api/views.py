from rest_framework import generics
from Jobs.models import Jobs
from .serializers import JobSerializer

class JobList(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer


class FailedJobList(generics.ListCreateAPIView):
    queryset = Jobs.failedJobObjects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer