from django.urls import path
from . views import StudentCreateAPI,StudentAPI,UpdateStudentAPI,DeleteStudentAPI, RetrieveStudentAPI
from .api import RegistrationAPI,LoginAPI

urlpatterns = [
    path('create',StudentCreateAPI.as_view()),
    path('registration',RegistrationAPI.as_view()),
    path('',StudentAPI.as_view()),
    path('login/',LoginAPI.as_view()),
    path('update/<int:pk>',UpdateStudentAPI.as_view()),
    path('delete/<int:pk>',DeleteStudentAPI.as_view()),
    path('get/<int:pk>/',RetrieveStudentAPI.as_view()),
]
