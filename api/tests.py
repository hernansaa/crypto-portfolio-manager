from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

class HealthCheckTests(TestCase):
    def setUp(self):
        # Configura el cliente API para hacer peticiones
        self.client = APIClient()

    def test_health_check(self):
        # Llama al endpoint de health check
        url = reverse('health-check')
        response = self.client.get(url)

        # Verifica que la respuesta sea HTTP 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica que el contenido de la respuesta sea correcto
        self.assertEqual(response.data['status'], 'Healthy')

        # Verifica que los checks individuales están bien
        self.assertEqual(response.data['database'], 'Healthy')
