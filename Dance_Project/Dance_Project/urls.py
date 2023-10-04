"""Dance_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path,include

# urlpatterns = [
#     path("admin/", admin.site.urls),
    
# ]










from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework.schemas import get_schema_view, openapi
from django.views.generic import TemplateView
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from django.utils.crypto import get_random_string


def token():
    unique_id = get_random_string(length=32)
    return unique_id


token = token()


schema_view = get_schema_view(
    openapi.Info(
        title="Dance_Project",
        default_version='v1.0.0-staging',
        name='openapi-schema',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('Api/token/',
         jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('Api/token/refresh/',
         jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
    path('admin/', admin.site.urls),
    path("Dance/",include("Dance_App.urls")),
    path("User/",include("User_App.urls")),
    # path('Url_Upload',include('PAFORM.urls')),
    # path('swagger/' + token, schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/' + token, schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('' + token, schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]