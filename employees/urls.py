from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('employees/',EmployeeListCreateView.as_view(),name='employee-list-create'),
    path('employees/<int:pk>/',EmployeeRetrieveUpdateDeleteView.as_view(),name='employee-detail'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
