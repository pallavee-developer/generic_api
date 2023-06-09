from django.urls import path
from .api import EmployeeCreateAPI, EmployeeAPI,UpdateEmployeeAPI,DeleteEmployeeAPI,EmployeeRetrieveAPI

urlpatterns = [
    path('api/create',EmployeeCreateAPI.as_view()),
    path('',EmployeeAPI.as_view()),
    path('api/<int:pk>',UpdateEmployeeAPI.as_view()),
    path('api/delete/<int:pk>',DeleteEmployeeAPI.as_view()),
    path('api/get/<int:pk>',EmployeeRetrieveAPI.as_view()),
    


]
