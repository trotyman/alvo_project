from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class AlvoAPITestCase(APITestCase):
    def test_criar_alvo_via_api(self):
        url = reverse('alvo-list')
        dados = {
            "identificador": "api001",
            "nome": "Alvo via API",
            "latitude": -10.0,
            "longitude": -50.0,
            "data_expiracao": "2025-12-31T23:59:59Z"
        }
        resposta = self.client.post(url, dados, format='json')
        self.assertEqual(resposta.status_code, status.HTTP_201_CREATED)
