from rest_framework import serializers
from .models import *



## userAccount

class userAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountModels
        fields = '__all__'



## login
class LoginSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountModels
        fields = ['username','password']



## userRole

class userRoleSerializers(serializers.ModelSerializer):

    class Meta:
        model = userRolesModels
        fields = '__all__'


## director

class directorSerializers(serializers.ModelSerializer):

    class Meta:
        model = directorModels
        fields = '__all__'



## coach

class coachSerializers(serializers.ModelSerializer):

    class Meta:
        model = coachModels
        fields = '__all__'




## userAccountRoles

class userAccountRolesSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountRolesModels
        fields = '__all__'






















