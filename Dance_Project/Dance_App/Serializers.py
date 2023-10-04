from rest_framework import serializers
from .models import *



## ageGroup

class ageGroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = ageGroupModels
        fields = '__all__'



## performance

class performanceSerializers(serializers.ModelSerializer):

    class Meta:
        model = performanceModels
        fields = ['artistId','description','location','date']
    def create(self, validated_data):
        a = performanceModels.objects.create(artistId=validated_data['artistId'],
                                       description=validated_data['description'],
                                       date=validated_data['date'],
                                       location=validated_data['location'],
                                       role="artist"
                                       )
        a.save()
        return a


class getperformanceSerializers(serializers.ModelSerializer):

    class Meta:
        model = performanceModels
        fields = ['id','artistId','description','location','date','role']
## attendanceRecord

class attendanceRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = attendanceRecordModels
        fields = ['date','status','artistId']
    def create(self, validated_data):
        a = attendanceRecordModels.objects.create(artistId=validated_data['artistId'],
                                             status=validated_data['status'],
                                             date=validated_data['date'],
                                             role="artist"
                                             )
        a.save()
        return a

class getattendanceRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = attendanceRecordModels
        fields = ['id','date','status','artistId','role']




## injuryRecord

class injuryRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = injuryRecordModels
        fields = ['date','injuryDescription','artistId']

    def create(self, validated_data):
        a = injuryRecordModels.objects.create(artistId=validated_data['artistId'],
                                             injuryDescription=validated_data['injuryDescription'],
                                             date=validated_data['date'],
                                             role="artist"
                                             )
        a.save()
        return a

class getinjuryRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = injuryRecordModels
        fields = ['id','date','injuryDescription','artistId','role']


## clubActivities

class clubActivitiesSerializers(serializers.ModelSerializer):

    class Meta:
        model = clubActivitiesModels
        fields = ['activityName','date','artistId','description',]

    def create(self, validated_data):
        a = clubActivitiesModels.objects.create(artistId=validated_data['artistId'],
                                              activityName=validated_data['activityName'],
                                              description=validated_data['description'],
                                              date=validated_data['date'],
                                              role="artist"
                                              )
        a.save()
        return a



class getclubActivitiesSerializers(serializers.ModelSerializer):

    class Meta:
        model = clubActivitiesModels
        fields = ['id','activityName','date','artistId','description','role']
