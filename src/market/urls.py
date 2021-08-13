from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'market', views.MarketApkViewSet)



urlpatterns = [
    path('', views.index, name='market'),
    path('details/<apk_id>', views.details, name='details'),
]