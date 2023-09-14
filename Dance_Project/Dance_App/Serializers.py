from rest_framework import serializers
from .models import *



## ageGroup

class ageGroupSerializers(serializers.ModelSerializer):

    class Meta:
        model = ageGroupModels
        fields = '__all__'


## artist

class artistSerializers(serializers.ModelSerializer):

    class Meta:
        model = artistModels
        fields = '__all__'



## performance

class performanceSerializers(serializers.ModelSerializer):

    class Meta:
        model = performanceModels
        fields = '__all__'



## attendanceRecord

class attendanceRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = attendanceRecordModels
        fields = '__all__'




## injuryRecord

class injuryRecordSerializers(serializers.ModelSerializer):

    class Meta:
        model = injuryRecordModels
        fields = '__all__'



## clubActivities

class clubActivitiesSerializers(serializers.ModelSerializer):

    class Meta:
        model = clubActivitiesModels
        fields = '__all__'




