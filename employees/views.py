from rest_framework import serializers
from .serializers import EmployeeSerializer
from  .models import Employee
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        department = self.request.query_params.get('department')
        role = self.request.query_params.get('role')
        if department:
            queryset = queryset.filter(department=department)
        if role:
            queryset = queryset.filter(role=role)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        return response

