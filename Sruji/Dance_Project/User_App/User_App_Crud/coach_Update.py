from django.shortcuts import render
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import generics



class coach_Update(generics.GenericAPIView):
    serializer_class = coachSerializers

    def put(self,request,id):

        try:

            a = coachModels.objects.get(id=id)
            b = coachSerializers(a, data=request.data)
            b.is_valid(raise_exception=True)
            data = b.save()
            return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Result" : coachSerializers(data).data
            })
        
        except Exception as e:
            error_message = str(e)  # Get the error message as a string
            return Response({
                "Message": "Fail",
                "Status": 400,
                "Result": error_message  # Include the error message in the response
            })