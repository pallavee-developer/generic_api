from django.urls import path
from .api import EmployeeCreateAPI, EmployeeAPI

urlpatterns = [
    path('api/create',EmployeeCreateAPI.as_view()),
    path('',EmployeeAPI.as_view()),

]
