from django.contrib.auth.models import Group, User

from portfolios.models import Portfolio, PortfolioTransaction
from market_data.models import Asset

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ['name', 'price_usd']


class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['name', 'initial_value', 'total_value']


class PortfolioTrasactionSerializer(serializers.HyperlinkedModelSerializer):
    #asset = serializers.HyperlinkedRelatedField(view_name='asset-detail', queryset=Asset.objects.all())

    class Meta:
        model = PortfolioTransaction
        fields = ['url', 'portfolio', 'asset', 'transaction_type', 'quantity', 'transaction_date', 'price_at_transaction', 'fees', 'total_value']
