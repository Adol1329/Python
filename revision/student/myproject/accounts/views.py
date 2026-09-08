from email.policy import HTTP

from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import AccountsSerializer


@api_view(["Post"])
def account_api(request):
    if request.method=="POST":
        serializer = AccountsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        