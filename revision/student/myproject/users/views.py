from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model

from .serializers import UserSerializer


User = get_user_model()


@api_view(["GET", "POST"])
def user_api(request):

    # GET ALL USERS
    if request.method == "GET":

        users = User.objects.all()

        serializer = UserSerializer(
            users,
            many=True
        )

        return Response(serializer.data)

    # CREATE USER
    if request.method == "POST":

        serializer = UserSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )