from django.urls import path, include 
from rest_framework import routers 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api import views

router = routers.DefaultRouter()	
router.register(r'Programadores', views.ProgramadoresViewSets)

urlpatterns = [
    path('', include(router.urls)),
]
