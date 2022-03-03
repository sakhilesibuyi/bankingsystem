from __future__ import unicode_literals
from distutils.log import log
from urllib import request
from wsgiref.util import request_uri
from django.http import QueryDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
import jwt, datetime
from rest_framework import generics

from .models import *
from .serializers import *

from .decorators import user_logged_in
from rest_framework.decorators import api_view


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LogOutView(APIView):
    def post(self,request):
        response = Response()
        request.user.auth_token.delete()
        response.data = {
            "message":"success"
        }
        return response
   
class BranchView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BankView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,) 
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class ClientView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AccountTypeView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer