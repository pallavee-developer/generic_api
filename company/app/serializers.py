from rest_framework import serializers
from . models import *

class EmployeeSerializer(serializers.ModelSerializer):
    model = Employee
    fields = '__all__'