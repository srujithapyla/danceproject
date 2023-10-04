from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from ..models import *
from ..Serializers import *
from rest_framework.response import Response
from rest_framework import generics



class clubActivities_Update(generics.GenericAPIView):
    serializer_class = clubActivitiesSerializers
    permission_classes = (IsAuthenticated,)

    def put(self,request,id):

        try:

            a = clubActivitiesModels.objects.get(id=id)
            b = clubActivitiesSerializers(a, data=request.data)
            b.is_valid(raise_exception=True)
            data = b.save()
            return Response({
                "Message" : "Successfull",
                "Status" : 200,
                "Result" : getclubActivitiesSerializers(data).data
            })
        
        except Exception as e:
            error_message = str(e)  # Get the error message as a string
            return Response({
                "Message": "Fail",
                "Status": 400,
                "Result": error_message  # Include the error message in the response
            })