from django.shortcuts import render
from rest_framework import generics
from . models import *
from . serializers import StudentSerializer

# Create your views here.
class StudentCreateAPI(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentAPI(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentAPI(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class DeleteStudentAPI(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class RetrieveStudentAPI(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


