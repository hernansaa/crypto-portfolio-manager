from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)
router.register(r"portfolios", views.PorfolioViewSet)
router.register(r"assets", views.AssetViewSet)
router.register(r"portfolio_transactions", views.PorfolioTransactionViewSet)


urlpatterns = [
    path("", views.api_root, name="api-root"),  # Map root URL "/" to api_root view
    path("api/", views.api_root),  # Custom API root view
    path("api/api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/health/", views.health_check, name="health-check"),
    path("api/", include(router.urls)),
]
