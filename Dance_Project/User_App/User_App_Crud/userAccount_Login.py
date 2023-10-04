import requests
from django.shortcuts import render
from ..serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from ..models import *
from django.contrib.auth.hashers import check_password







url='http://127.0.0.1:8000/'
def logintoken():
    api = url + "Api/token/"
    headers = {'Content-Type': 'application/json'}
    # null = None
    post = {
        "username": "dance",
        "password": "dance@1",
    }
    r = requests.post(api, json=post, headers=headers)
    data = r.json()
    return data






## Login

class Login(generics.GenericAPIView):
    serializer_class = LoginSerializers


    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        a = logintoken()
        access = a["access"]
        if username.endswith('.com'):
            a = userAccountModels.objects.get(email=username)
            if check_password(password, a.password):
                return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Result" : GetuserAccountSerializers(a).data,
                "BearerToken":access

            })
            else:
                return Response({
                "Message" : "invalid username",
                "Status" : 400,
                "Result" : []

            })

        elif userAccountModels.objects.get(username=username):
            a=userAccountModels.objects.get(username=username)
            if check_password(password, a.password):
             return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Result" : LoginSerializers(a).data,
                "BearerToken": access

            })

            else:
                return Response({
                            "Message" : "invalid Password/username",
                            "Status" : 400,
                            "Result" : []

                        })

        else:
            return Response({
                "Message" : "fail",
                "Status" : 400,
                "Result" : []

            })







       