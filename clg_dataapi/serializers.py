from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import StudentData, TeacherData, Branch

class TeacherDataSerializers(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()

    class  Meta:
        model = TeacherData
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'

class StudentDataSerializers(serializers.ModelSerializer):
    branch = serializers.StringRelatedField()
    teacher_name = serializers.StringRelatedField()
    class  Meta:
        model = StudentData
        fields = '__all__'
