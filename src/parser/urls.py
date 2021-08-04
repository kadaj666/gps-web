from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from market.urls import router as market_router
    
router = routers.DefaultRouter(trailing_slash=False)
router.registry.extend(market_router.registry)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('market.urls')),
]