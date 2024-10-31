from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class LoginView(generics.GenericAPIView):
	
	serializer_class=LoginSerializer
	
	def post(self,request):
                try:
                    data = request.data
                    serializer = self.get_serializer(data=data)
                    serializer.is_valid(raise_exception=True)
                    response = serializer.get_jwt_token(serializer.validated_data)
                    return Response(response, status=status.HTTP_200_OK)
        
                except serializers.ValidationError as e:
                    return Response({"data": e.detail, "message": "Invalid credentials..!"}, status=status.HTTP_400_BAD_REQUEST)

                except Exception as e:
                    return Response({"data": {}, "message": "Something went wrong..!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
                

                
