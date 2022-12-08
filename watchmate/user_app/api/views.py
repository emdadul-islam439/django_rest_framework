from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import RegistrationSerializer
from user_app import models

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.get(user=account).key
            status_code = status.HTTP_201_CREATED
            
            data['Response'] = "User created successfully!"
            data['username'] = account.username
            data['email'] = account.email
            data['token'] = token
        else:
            data = serializer.errors
            status_code = status.HTTP_400_BAD_REQUEST
        
        return Response(data, status=status_code)
    

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)