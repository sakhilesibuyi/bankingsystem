from __future__ import unicode_literals
from distutils.log import log
from urllib import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

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


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        #get user
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not Found')
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect User Password")
        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.now()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')

        response = Response()
        response.set_cookie(key='token',value=token,httponly=True)
        response.data = {
            'token':token,
        }
        return response
class LogOutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            "message":"success"
        }
        return response
@user_logged_in
@api_view(['GET', 'POST'])
def BranchView(request):
    if request.method == 'POST': #(self,request):
        serializer = BranchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)       
    if request.method == 'GET': #(self,request):
        branches = Branch.objects.all()
        serializers = BranchSerializer(branches, many=True)
        return Response(serializers.data)

"""class BranchView(APIView):
    def post(self,request):
        serializer = BranchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)       
    def get(self,request):
        branches = Branch.objects.all()
        serializers = BranchSerializer(branches, many=True)
        return Response(serializers.data) """