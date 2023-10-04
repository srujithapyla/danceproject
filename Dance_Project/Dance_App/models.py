from django.db import models
from django.apps import apps

## ageGroup

class ageGroupModels(models.Model):
    ageRange = models.CharField(max_length=100)
    objects = models.Manager()


    class Meta:
        db_table = "ageGroup_table"  


## performance

class performanceModels(models.Model):

    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    artistId = models.ForeignKey("User_App.userAccountModels", max_length=250, related_name='performance',
                                   on_delete=models.CASCADE, default=True)
    role =models.CharField(max_length=100)


    class Meta:
        db_table = "Performance_table"



## attendanceRecord

class attendanceRecordModels(models.Model):
    
    date = models.DateTimeField()
    status = models.CharField(max_length=100)
    artistId = models.ForeignKey("User_App.userAccountModels", max_length=250, related_name='attendanceRecord',
                                   on_delete=models.CASCADE, default=True)
    role = models.CharField(max_length=100)



    class Meta:
        db_table = "attendanceRecord_table"




## injuryRecord

class injuryRecordModels(models.Model):

    date = models.DateTimeField()
    injuryDescription = models.CharField(max_length=500)
    artistId = models.ForeignKey("User_App.userAccountModels", max_length=250, related_name='injuryRecord',
                                   on_delete=models.CASCADE, default=True)
    role = models.CharField(max_length=100)



    class Meta:
        db_table = "injuryRecord_table"
    


## clubActivities

class clubActivitiesModels(models.Model):

    activityName = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.CharField(max_length=500)
    artistId = models.ForeignKey("User_App.userAccountModels", max_length=250, related_name='clubActivities',
                                   on_delete=models.CASCADE, default=True)
    role = models.CharField(max_length=100)


    class Meta:
        db_table = "clubActivities_table"


