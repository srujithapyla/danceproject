from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [

    ## ageGroup

    path("ageGroup/", ageGroup.as_view()),
    path("ageGroup_get/",ageGroup_get.as_view()),
    path("ageGroup_get/<int:id>",ageGroup_get.as_view()),
    path("ageGroup_update/<int:id>",ageGroup_Update.as_view()),

    ## performance

    path("performance/", performance.as_view()),
    path("performance_get/",performance_get.as_view()),
    path("performance_get/<int:id>",performance_get.as_view()),
    path("performance_update/<int:id>",performance_Update.as_view()),


    ## attendanceRecord

    path("attendanceRecord/", attendanceRecord.as_view()),
    path("attendanceRecord_get/",attendanceRecord_get.as_view()),
    path("attendanceRecord_get/<int:id>",attendanceRecord_get.as_view()),
    path("attendanceRecord_update/<int:id>",attendanceRecord_Update.as_view()),



    ## injuryRecord

    path("injuryRecord/", injuryRecord.as_view()),
    path("injuryRecord_get/",injuryRecord_get.as_view()),
    path("injuryRecord_get/<int:id>",injuryRecord_get.as_view()),
    path("injuryRecord_update/<int:id>",injuryRecord_Update.as_view()),



    ## clubActivities

    path("clubActivities/", clubActivities.as_view()),
    path("clubActivities_get/",clubActivities_get.as_view()),
    path("clubActivities_get/<int:id>",clubActivities_get.as_view()),
    path("clubActivities_update/<int:id>",clubActivities_Update.as_view()),



]
