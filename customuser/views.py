import jwt
from jwt.exceptions import ExpiredSignatureError, DecodeError

from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS

from .serializer import UserSerializer
from .utils import Utils

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        permissions = []
        if self.request in SAFE_METHODS:
            permissions.append(IsAdminUser)
        return [permission() for permission in permissions]


class RegisterUser(APIView):
    serializer_class = UserSerializer
    utility = Utils()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = self.utility.generate_confirmation_token(user)
        current_site = get_current_site(request).domain
        subject = 'Verify Email'
        template_data = {
            'request': request,
            'user': request.user,
            'domain': current_site,
            'token': token,
        }

        message = render_to_string('customuser/verify_email_message.html', template_data)
        email_data = {
            'email_message': message,
            'email_subject': subject,
            'email': user.email
        }
        self.utility.send_email(email_data)

        return Response({'message': 'User registered successfully. Please check your email for verification link'}, status=status.HTTP_201_CREATED)
    

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'old_password' in request.data:
            user = authenticate(request=request, email=request.data.get('email'), password=request.data.get('password'))
                
        serializer = self.get_serializer(instance=instance, data = request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()


class SingUp(APIView):
    pass
    

class VerifyEmail(APIView):
    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        try:
            token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(pk=token['user_id'])
            if user:
                user.is_active = True
                user.save()
                return Response({'message': 'Email is successfully verified'}, status=status.HTTP_200_OK)
        except ExpiredSignatureError:
            return Response({'error': 'Activation token has Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        

        
