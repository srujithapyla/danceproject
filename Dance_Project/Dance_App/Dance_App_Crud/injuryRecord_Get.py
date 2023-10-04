from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..Serializers import *
from rest_framework.response import Response
from rest_framework import generics



class injuryRecord_get(generics.GenericAPIView):
    serializer_class = injuryRecordSerializers
    permission_classes = (IsAuthenticated,)

    def get(self,request,id=None):

        try:
            if id:
                b = injuryRecordModels.objects.filter(id=id)
            else:
                b = injuryRecordModels.objects.all()
            s = getinjuryRecordSerializers(b, many=True)
            if b:
                return Response({
                    "Message" : "Successfull",
                    "Status" : 200,
                    "Result" : s.data
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
        


        