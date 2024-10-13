from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (CreateAPIView
                                    ,RetrieveAPIView
                                    ,ListAPIView
                                    ,RetrieveDestroyAPIView
                                    ,RetrieveUpdateAPIView
                                    ) 
from user.models import User
from rest_framework.permissions import AllowAny
from user.serializers import RegisterSerializer,UserGetSerializer,UserPutSerializer
from rest_framework.response import Response
# Create your views here.


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserUpdateView(APIView):
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def get(self,request,format=None):
        print(request.user)
        user = User.objects.filter(pk=request.user.id)

        return Response(RegisterSerializer(user,many=True).data)
    def put(self, request, format=None):
        qs = User.objects.get(pk=request.user.id)
        serializer = UserPutSerializer(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
