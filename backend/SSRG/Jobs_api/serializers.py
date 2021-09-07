from rest_framework import serializers
from Jobs.models import Jobs


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id', 'files','uploadDate','language','baseFile','emailNow','jobState','user','jobRef')
    #Jobs.jobRef = str(Jobs.uploadDate)
    #Jobs.jobRef = Jobs.jobRef[2]+Jobs.jobRef[3]+Jobs.jobRef[5]+Jobs.jobRef[6]+Jobs.jobRef[8]+Jobs.jobRef[9]+Jobs.jobRef[11]+Jobs.jobRef[12]+Jobs.jobRef[14]+Jobs.jobRef[15]+Jobs.jobRef[17]+Jobs.jobRef[18]+Jobs.jobRef[20]+Jobs.jobRef[21]+Jobs.jobRef[22]+Jobs.jobRef[23]
