from django.shortcuts import render
from account.permissions import IsSuperUser

from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView
                                    ,RetrieveAPIView
                                    ,ListAPIView
                                    ,RetrieveDestroyAPIView
                                    ,RetrieveUpdateAPIView
                                    ) 
from account.models import CheckingAccount,SavingAccount,Transaction
from rest_framework.permissions import AllowAny
from account.serializers import CheckingAccountSerializer,SavingAccountSerializer,TransactionSerializer,TransactionPostSerializer
from rest_framework.response import Response
from django.db import IntegrityError, transaction

# Create your views here.


class TransactionList(ListAPIView):
    queryset=Transaction.objects.all().order_by('-id')[:10]          
    serializer_class=TransactionSerializer
class TransactionCreate(CreateAPIView):
    queryset=Transaction.objects.all()
    serializer_class=TransactionPostSerializer
    # permission_classes=(IsSuperUser,)
    def get_form_kwargs(self):
        kwargs=super(TransactionCreate,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user,
        })
        return kwargs
    # def post(self, request, format=None):
    #     # qs = Transaction.objects.get(pk=request.user.id)
    #     serializer = TransactionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)


class CheckingAccountCreate(CreateAPIView):
    queryset=CheckingAccount.objects.all()
    serializer_class=CheckingAccountSerializer
    permission_classes=(IsSuperUser,)
    def get_form_kwargs(self):
        kwargs=super(TransactionCreate,self).get_form_kwargs()
        kwargs.update({
            'user':self.request.user,
        })
        return kwargs
class CheckingAccountUpdate(RetrieveUpdateAPIView):
    queryset=CheckingAccount.objects.all()
    serializer_class=CheckingAccountSerializer

class SavingAccountCreate(CreateAPIView):
    queryset=SavingAccount.objects.all()
    serializer_class=SavingAccountSerializer
    permission_classes=(IsSuperUser,)
