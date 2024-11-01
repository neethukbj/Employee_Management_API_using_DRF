from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=["username","password","first_name","last_name"]


	def validate(self,data):
		if User.objects.filter(username=data["username"]).exists():
			raise serializers.ValidationError("User already Exists...!")
		return data


	def create(self,validated_data):
		user=User.objects.create(username=validated_data['username'],
			first_name=validated_data['first_name'],
			last_name=validated_data['last_name']
			)
		user.set_password(validated_data['password'])
		user.save()
		return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


    def validate(self,data):
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("no user account..!")  
        return data
    
    def get_jwt_token(self,data):
        user = authenticate(username=data['username'],password=data['password'])
        
        if not user:
            return {"message": "The user account is not valid..!","data":{}}        
        refresh = RefreshToken.for_user(user)
        return {"message":"login success","data":{"token":{},"refresh":str(refresh),"access":str(refresh.access_token),}}