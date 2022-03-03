from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id','username','email','password']
        #we do not want to return the password after successful registration
        extra_kwargs = {
            'password':{'write_only':True} 
        }
    #Ensure the password value is hidden
    def create(self, validated_data):
        #Performing hashing on the password instance
        password = validated_data.pop('password',None) # pop out the password from the validated data
        instance = self.Meta.model(**validated_data) # get the instance without the extracted password
        if password is not None:
            instance.set_password(password) #hash it
        instance.save() 
        return instance
    
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['branch_name','branch_code','id']

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('__all__')
    def to_representation(self, instance):
        response =  super().to_representation(instance)
        response['branch'] = BranchSerializer(instance.branch).data
        return response
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields =('__all__')

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = (__all__)       