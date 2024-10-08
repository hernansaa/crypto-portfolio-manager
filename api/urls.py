from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'portfolios', views.PorfolioViewSet)
router.register(r'assets', views.AssetViewSet)
router.register(r'portfolio_transactions', views.PorfolioTransactionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', views.api_root),  # Custom API root view
    path('api/health/', views.health_check, name='health-check'),
    path('api/', include(router.urls)),
]


