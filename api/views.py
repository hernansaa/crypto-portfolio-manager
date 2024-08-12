from django.shortcuts import render
from django.contrib.auth.models import Group, User

from portfolios.models import Portfolio, PortfolioTransaction
from market_data.models import Asset

from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer, AssetSerializer, PortfolioSerializer, PortfolioTrasactionSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated] 


class AssetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Asset.objects.all().order_by('name')
    serializer_class = AssetSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'name'  # Ensure this matches the serializer


class PorfolioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Portfolio.objects.all().order_by('name')
    serializer_class = PortfolioSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class PorfolioTransactionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PortfolioTransaction.objects.all().order_by('-transaction_date')
    serializer_class = PortfolioTrasactionSerializer
    permission_classes = [permissions.IsAuthenticated]