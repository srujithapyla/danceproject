from django.shortcuts import render

## userAccount
from .User_App_Crud.userAccount_Register import userAccount
from .User_App_Crud.userAccount_Login import Login
from .User_App_Crud.userAccount_Get import userAccount_get
from .User_App_Crud.userAccount_Update import userAccount_Update

## userRoles
from .User_App_Crud.userRoles_Post import userRoles
from .User_App_Crud.userRoles_Get import userRoles_get
from .User_App_Crud.userRoles_Update import userRoles_Update


## director
from .User_App_Crud.director_Post import director
from .User_App_Crud.director_Get import director_get
from .User_App_Crud.director_Update import director_Update


## coach
from .User_App_Crud.coach_Post import coach
from .User_App_Crud.coach_Get import coach_get
from .User_App_Crud.coach_Update import coach_Update


## userAccountRoles
from .User_App_Crud.userAccountRoles_Post import userAccountRoles
from .User_App_Crud.userAccountRoles_Get import userAccountRoles_get
from .User_App_Crud.userAccountRoles_Update import userAccountRoles_Update





##userAccount

userAccount()
Login()
userAccount_get()
userAccount_Update()


## userRoles

userRoles()
userRoles_get()
userRoles_Update()


## director
director()
director_get()
director_Update()


## coach
coach()
coach_get()
coach_Update()


## userAccountRoles
userAccountRoles()
userAccountRoles_get()
userAccountRoles_Update()





