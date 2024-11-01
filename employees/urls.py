from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('employees/',EmployeeListCreateView.as_view(),name='employee-list-create'),
    path('employees/<int:pk>/',EmployeeRetrieveUpdateDeleteView.as_view(),name='employee-detail'),
]
