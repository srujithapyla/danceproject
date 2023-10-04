from django.shortcuts import render
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.hashers import make_password

class userAccount_Update(generics.GenericAPIView):
    serializer_class = updateuserAccountSerializers

    def put(self, request, id):
        try:
            a = userAccountModels.objects.get(id=id)
            b = updateuserAccountSerializers(a, data=request.data)

            if 'password' in request.data:
                request.data['password'] = make_password(request.data['password'])

            b.is_valid(raise_exception=True)
            data = b.save()
            return Response({
                "Message": "Successful",
                "Status": 200,
                "Result": GetuserAccountSerializers(data).data
            })

        except Exception as e:
            error_message = str(e)  # Get the error message as a string
            return Response({
                "Message": "Fail",
                "Status": 400,
                "Result": error_message  # Include the error message in the response
            })
