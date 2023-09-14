from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [

    ## userAccount

    path("userAccountRegister/", userAccount.as_view()),
    path("userAccountLogin/",Login.as_view()),
    path("userAccount_get/", userAccount_get.as_view()),
    path("userAccount_get/<int:id>", userAccount_get.as_view()),
    path("userAccount_Update/<int:id>",userAccount_Update.as_view()),



## userRoles
    path("userRoles/", userRoles.as_view()),
    path("userRoles_get/", userRoles_get.as_view()),
    path("userRoles_get/<int:id>", userRoles_get.as_view()),
    path("userRoles_Update/<int:id>",userRoles_Update.as_view()),



## director
    path("director/", director.as_view()),
    path("director_get/", director_get.as_view()),
    path("director_get/<int:id>", director_get.as_view()),
    path("director_Update/<int:id>",director_Update.as_view()),


## coach
    path("coach/", coach.as_view()),
    path("coach_get/", coach_get.as_view()),
    path("coach_get/<int:id>", coach_get.as_view()),
    path("coach_Update/<int:id>",coach_Update.as_view()),



## userAccountRoles
    path("userAccountRoles/", userAccountRoles.as_view()),
    path("userAccountRoles_get/", userAccountRoles_get.as_view()),
    path("userAccountRoles_get/<int:id>", userAccountRoles_get.as_view()),
    path("userAccountRoles_Update/<int:id>",userAccountRoles_Update.as_view()),



]    