from rest_framework import generics
from Jobs.models import Jobs
from .serializers import JobSerializer

class JobList(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Jobs.objects.filter(user = user)
    
        #Jobs.jobRef = Jobs.jobRef[2]+Jobs.jobRef[3]+Jobs.jobRef[5]+Jobs.jobRef[6]+Jobs.jobRef[8]+Jobs.jobRef[9]+Jobs.jobRef[11]+Jobs.jobRef[12]+Jobs.jobRef[14]+Jobs.jobRef[15]+Jobs.jobRef[17]+Jobs.jobRef[18]+Jobs.jobRef[20]+Jobs.jobRef[21]+Jobs.jobRef[22]+Jobs.jobRef[23]


class FailedJobList(generics.ListAPIView):
    queryset = Jobs.failedJobObjects.all()
    serializer_class = JobSerializer

class JobDetail(generics.RetrieveDestroyAPIView):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

class PendingJobList(generics.ListAPIView):
    queryset = Jobs.pendingJobObjects.all()
    serializer_class = JobSerializer

class SuccessJobList(generics.ListAPIView):
    queryset = Jobs.successJobObjects.all()
    serializer_class = JobSerializer