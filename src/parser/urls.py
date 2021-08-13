from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from market.urls import router as market_router
from django.contrib.auth import views as auth_views
from .forms import UserLoginForm

router = routers.DefaultRouter(trailing_slash=False)
router.registry.extend(market_router.registry)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('market.urls')),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html', authentication_form=UserLoginForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
]