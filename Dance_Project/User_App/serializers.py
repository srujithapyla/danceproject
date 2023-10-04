from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password



## userAccount

class userAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountModels
        fields = ['username','password','email','name','age','personalinfo']
    def create(self, validated_data):
        a=userAccountModels.objects.create(username=validated_data['username'],
                                           password=(make_password(validated_data['password'])),
                                           email=validated_data['email'],
                                           name=validated_data['name'],
                                           age=validated_data['age'],
                                           personalinfo=validated_data['personalinfo'],
                                           role="user"
                                           )
        a.save()
        return a

class updateuserAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountModels
        fields = ['username','password','email','name','age','personalinfo']
    def create(self, validated_data):
        a=userAccountModels.objects.create(username=validated_data['username'],
                                           password=(make_password(validated_data['password'])),
                                           email=validated_data['email'],
                                           name=validated_data['name'],
                                           age=validated_data['age'],
                                           personalinfo=validated_data['personalinfo'],
                                           role="user"
                                           )
        a.save()
        print(a.password)
        return a

class GetuserAccountSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountModels
        fields = ['id','username','password','email','name','age','personalinfo','role']



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
        fields = ['director_name','director_contactInfo','userId']

    def create(self, validated_data):
        a = directorModels.objects.create(director_name=validated_data['director_name'],
                                       director_contactInfo=validated_data['director_contactInfo'],
                                       userId=validated_data['userId'],
                                       role="director"
                                       )
        a.save()
        return a

class getdirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = directorModels
        fields = ['id','director_name','director_contactInfo','userId','role']

## coach

class coachSerializers(serializers.ModelSerializer):

    class Meta:
        model = coachModels
        fields = ['coach_name','coach_contactInfo','userId']

    def create(self, validated_data):
        a = coachModels.objects.create(coach_name=validated_data['coach_name'],
                                             coach_contactInfo=validated_data['coach_contactInfo'],
                                             userId=validated_data['userId'],
                                             role="coach"
                                             )
        a.save()
        return a



class getcoachSerializers(serializers.ModelSerializer):
    class Meta:
        model = coachModels
        fields = ['id','coach_name','coach_contactInfo','userId','role']

## userAccountRoles

class userAccountRolesSerializers(serializers.ModelSerializer):

    class Meta:
        model = userAccountRolesModels
        fields = '__all__'






















