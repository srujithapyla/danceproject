from django.shortcuts import render
from ..serializers import *
from rest_framework import generics
from rest_framework.response import Response
from django.http import HttpResponse
from ..models import *


## Registration

class userAccount(generics.GenericAPIView):
    serializer_class = userAccountSerializers

    def post(self,request):
        try:
            p = userAccountSerializers(data=request.data)
            p.is_valid(raise_exception=True)
            k = p.save()
            return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Response" : GetuserAccountSerializers(k).data

            })
        
        except Exception as e:
            error_message = str(e)
            return Response({
                "Message" : "Fail",
                "Status" : 400,
                "Result" : error_message
            })