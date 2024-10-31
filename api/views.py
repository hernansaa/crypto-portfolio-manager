from django.shortcuts import render
from django.contrib.auth.models import Group, User
from django.db import connection

from portfolios.models import Portfolio, PortfolioTransaction
from market_data.models import Asset

from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .serializers import (
    GroupSerializer,
    UserSerializer,
    AssetSerializer,
    PortfolioSerializer,
    PortfolioTrasactionSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """

#     queryset = Group.objects.all().order_by("name")
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Asset.objects.all().order_by("name")
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'name'  # Ensure this matches the serializer


class PorfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Portfolio.objects.all().order_by("name")
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]


class PorfolioTransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = PortfolioTransaction.objects.all().order_by("-transaction_date")
    serializer_class = PortfolioTrasactionSerializer
    permission_classes = [permissions.AllowAny]


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def health_check(request):

    # Check database connection
    try:
        connection.ensure_connection()
        db_status = "Healthy"
    except Exception as e:
        db_status = f"Unhealthy: {str(e)}"

    return Response(
        {
            "status": "Healthy" if db_status == "Healthy" else "Unhealthy",
            "database": db_status,
        }
    )


@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def api_root(request, format=None):
    return Response(
        {
            "health": reverse("health-check", request=request, format=format),
            "users": reverse("user-list", request=request, format=format),
            # "groups": reverse("group-list", request=request, format=format),
            "portfolios": reverse("portfolio-list", request=request, format=format),
            "assets": reverse("asset-list", request=request, format=format),
            "portfolio_transactions": reverse(
                "portfoliotransaction-list", request=request, format=format
            ),
        }
    )
