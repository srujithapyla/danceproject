from django.db import models
from django.apps import apps

## userAccount
class userAccountModels(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    personalinfo = models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    objects = models.Manager()

    class Meta:
        db_table = "userAccount_table"


## userRole
class userRolesModels(models.Model):
    roleName = models.CharField(max_length=100)
    objects = models.Manager()


    class Meta:
        db_table = "userRoles_table"


## director
class directorModels(models.Model):
    director_name = models.CharField(max_length=100)
    director_contactInfo = models.CharField(max_length=100)
    userId = models.ForeignKey(userAccountModels, max_length=250, related_name='director',
                                   on_delete=models.CASCADE, default=True)
    role = models.CharField(max_length=200)

    objects = models.Manager()


    class Meta:
        db_table = "dirtector_table"


## coach
class coachModels(models.Model):
    coach_name = models.CharField(max_length=100)
    coach_contactInfo = models.CharField(max_length=100)
    userId = models.ForeignKey(userAccountModels, max_length=250, related_name='coach',
                                   on_delete=models.CASCADE, default=True)
    role = models.CharField(max_length=200)
    objects = models.Manager()


    class Meta:
        db_table = "coach_table"




## userAccountRoles
class userAccountRolesModels(models.Model):
    userId = models.ForeignKey(userAccountModels, max_length=250, related_name='userAccount',
                                   on_delete=models.CASCADE, default=True)
    userRoleId = models.ForeignKey(userRolesModels, max_length=250, related_name='userRoles',
                                   on_delete=models.CASCADE, default=True)





