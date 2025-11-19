from rest_framework import serializers
from .models import DynamicForm, EmployeeRecord

class DynamicFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicForm
        fields = ['id','name','description','fields_json','created_by','created_at']
        read_only_fields = ['created_by','created_at']

class EmployeeRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRecord
        fields = ['id','form','data','created_by','created_at']
        read_only_fields = ['created_by','created_at']
