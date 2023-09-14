from django.shortcuts import render
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import generics



class coach_get(generics.GenericAPIView):
    serializer_class = coachSerializers

    def get(self,request,id=None):

        try:
            if id:
                a = coachModels.objects.filter(id=id)
            else:
                a = coachModels.objects.all()
            b = coachSerializers(a, many=True)  
            if a:
                return Response({
                    "Message" : "Successfull",
                    "Status" : 200,
                    "Result" : b.data
                }) 
             
            else:
                return Response({
                "Message" : "there is no data for this id",
                "Status" : 400,
                "Result" : "Invalid"
            })


        except Exception as e:
            error_message = str(e)  # Get the error message as a string
            return Response({
                "Message": "Fail",
                "Status": 400,
                "Result": error_message  # Include the error message in the response
            })
        


        