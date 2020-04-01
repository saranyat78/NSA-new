from rest_framework import serializers
from jsonfield.fields import JSONField
from .models import Tech, Tech1


class TechSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tech
        fields = ['DeviceIP', 'Account_Name', 'ConfigDifference']


class TechSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Tech1
        fields = ['DeviceIP', 'Account_Name', 'Average', 'BWUtilization']

