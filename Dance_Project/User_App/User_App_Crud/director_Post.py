from django.shortcuts import render
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import generics




class director(generics.GenericAPIView):
    serializer_class = directorSerializers

    def post(self,request):

        try:

            a = directorSerializers(data=request.data)
            a.is_valid(raise_exception=True)
            data = a.save()
            return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Result" : directorSerializers(data).data
            })


        except Exception as e:
            error_message = str(e)  # Get the error message as a string
            return Response({
                "Message": "Fail",
                "Status": 400,
                "Result": error_message  # Include the error message in the response
            })

