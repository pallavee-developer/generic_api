from django.urls import path
from . views import StudentCreateAPI,StudentAPI,UpdateStudentAPI,DeleteStudentAPI, RetrieveStudentAPI

urlpatterns = [
    path('create',StudentCreateAPI.as_view()),
    path('',StudentAPI.as_view()),
    path('update/<int:pk>',UpdateStudentAPI.as_view()),
    path('delete/<int:pk>',DeleteStudentAPI.as_view()),
    path('get/<int:pk>/',RetrieveStudentAPI.as_view()),
]
