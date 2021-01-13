from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from vedois.production import views


router = routers.DefaultRouter()
router.register(r'user-terminal', views.UserTerminalViewSet)

app_name = 'production'
urlpatterns = [
    path('api/', include(router.urls)),
]