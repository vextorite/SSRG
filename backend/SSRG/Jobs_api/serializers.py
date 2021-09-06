from rest_framework import serializers
from Jobs.models import Jobs

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'