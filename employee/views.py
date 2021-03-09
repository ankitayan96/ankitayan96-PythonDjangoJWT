from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework import permissions



class EmployeeListAPIView(ListCreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(manager=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(manager=self.request.user)


class EmployeeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Employee.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(manager=self.request.user)