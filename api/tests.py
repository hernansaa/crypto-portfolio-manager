from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User, Group
from portfolios.models import Portfolio, PortfolioTransaction
from market_data.models import Asset
from django.test import TestCase
from django.urls import reverse


class UserAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass")
        self.client.login(username="testuser", password="testpass")  # Log in the user to authenticate requests
    
    def test_get_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpass'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class GroupAPITests(APITestCase):
    def setUp(self):
        # Create a test user and log them in for authenticated requests
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass")
        self.client.login(username="testuser", password="testpass")
        
        # Create a test group for the tests
        self.group = Group.objects.create(name="Test Group")

    def test_get_groups(self):
        url = reverse('group-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# class PortfolioAPITests(APITestCase):
#     def setUp(self):
#         self.portfolio = Portfolio.objects.create(name="Test Portfolio", initial_value=1000, total_value=1500)

#     def test_get_portfolios(self):
#         url = reverse('portfolio-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class PortfolioTransactionAPITests(APITestCase):
#     def setUp(self):
#         self.portfolio = Portfolio.objects.create(name="Test Portfolio", initial_value=1000, total_value=1500)
#         self.asset = Asset.objects.create(name="Test Asset", price_usd=100)
#         self.transaction = PortfolioTransaction.objects.create(
#             portfolio=self.portfolio,
#             asset=self.asset,
#             transaction_type="buy",
#             quantity=10,
#             transaction_date="2023-01-01",
#             price_at_transaction=100,
#             fees=1.5,
#             total_value=1000,
#         )

#     def test_get_transactions(self):
#         url = reverse('portfoliotransaction-list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_create_transaction(self):
#         url = reverse('portfoliotransaction-list')
#         data = {
#             'portfolio': self.portfolio.id,
#             'asset': self.asset.id,
#             'transaction_type': 'buy',
#             'quantity': 5,
#             'transaction_date': '2023-01-02',
#             'price_at_transaction': 105,
#             'fees': 1.0,
#             'total_value': 525
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# class HealthCheckTests(TestCase):
#     def setUp(self):
#         # Configura el cliente API para hacer peticiones
#         self.client = APIClient()

#     def test_health_check(self):
#         # Llama al endpoint de health check
#         url = reverse('health-check')
#         response = self.client.get(url)

#         # Verifica que la respuesta sea HTTP 200 OK
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         # Verifica que el contenido de la respuesta sea correcto
#         self.assertEqual(response.data['status'], 'Healthy')

#         # Verifica que los checks individuales están bien
#         self.assertEqual(response.data['database'], 'Healthy')
