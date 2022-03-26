from django.shortcuts import render

from rest_framework.generics import ListAPIView
from rest_framework.response  import  Response
from .models import TeacherData, StudentData, Branch
from .serializers import TeacherDataSerializers, StudentDataSerializers, BranchSerializer
from rest_framework.filters import SearchFilter

from clg_dataapi import serializers
# Create your views here.

class  teacherView(ListAPIView):
    filter_backends= [SearchFilter]
    search_fields= ['tname']
    queryset = TeacherData.objects.all()
    serializer_class=TeacherDataSerializers
  
    
  
class branchView(ListAPIView):
    filter_backends= [SearchFilter]
    search_fields= ['branch']
    queryset= Branch.objects.all()
    serializer_class = BranchSerializer


class  StudentView(ListAPIView):
    filter_backends= [SearchFilter]
    search_fields= ['sname']
    serializer_class=StudentDataSerializers

    def get_queryset(self):
        tid = self.kwargs['tid']
        print(tid)
        queryset = StudentData.objects.filter(teacher_name=tid)

        return queryset



class  StudentsView(ListAPIView):
    filter_backends= [SearchFilter]
    search_fields= ['sname']
    queryset = StudentData.objects.all()
    serializer_class=StudentDataSerializers

    

    