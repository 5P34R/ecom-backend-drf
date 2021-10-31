from django.shortcuts import render
from django.contrib.auth import login

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer, LoginSerializer

class RegistrationView(APIView):
    def post(self, request):
        password = request.data['password']
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class LoginView(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request':request})
        # breakpoint()
        serializer.is_valid(raise_exception=True)  
        user = serializer.validated_data['user']
        if user:
            login(request, user)
            return Response({
            'status':True,
            'details':'Logined as user '+str(user)
        })
        return Response({
            'status':True,
            'detail':serializer.errors
        })