"""Plant_Nursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Nursery_API import views
#from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from SigninSignup.views import RegisterUserApi, RegisterNurseryApi

# router.register(r'upload', views.UploadViewSet, basename="upload")

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^api/Plants/$', views.PlantList.as_view(), name="plant_name"),
    url(r'^api/Plants/(?P<plant_id>\d+)/$', views.PlantDetail.as_view(), name="plant_name"),
    url(r'^api/Users/$', views.UserList.as_view(), name="user_list"),
    url(r'^api/Users/(?P<user_id>\d+)/$', views.UserDetail.as_view(), name="user_list"),
    url(r'^api/auth/$', views.UserAuthentication.as_view(), name='User Authentication API'),
    url(r'^api/Nursery/$', views.NurseryList.as_view(), name="nursery_list"),
    url(r'^api/Nursery/(?P<nursery_id>\d+)/$', views.NurseryDetail.as_view(), name="nursery_list"),
    url(r'^api/NurseryPlant/$', views.NurseryPlantList.as_view(), name="nursery_plant_list"),
    #url(r'^api/NurseryPlant/(?P<nursery_id>\d+)/$', views.NurseryPlantList.as_view(), name="nursery_list"),
    url(r'^api/UserPlant/$', views.UserPlantList.as_view(), name="user_plant_list"),
    url(r'^api/RegisterUser/$', RegisterUserApi.as_view(), name="user_reg"),
    url(r'^api/RegisterNursery/$', RegisterNurseryApi.as_view(), name="nursery_reg"),
    #url(r'^api/RegisterNursery/$', RegisterNurseryApi.as_view(), name="nursery_plant_list"),
    #path(r'^api/token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path(r'^api/token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)