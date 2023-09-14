from django.shortcuts import render
from ..models import *
from ..Serializers import *
from rest_framework.response import Response
from rest_framework import generics



class artist(generics.GenericAPIView):
    serializer_class = artistSerializers

    def post(self,request):

        try:

            a = artistSerializers(data=request.data)
            a.is_valid(raise_exception=True)
            data = a.save()
            return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Result" : artistSerializers(data).data
            })


        except Exception as e:
            error_message = str(e)  # Get the error message as a string
            return Response({
                "Message": "Fail",
                "Status": 400,
                "Result": error_message  # Include the error message in the response
            })