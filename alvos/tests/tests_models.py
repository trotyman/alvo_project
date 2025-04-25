from django.test import TestCase
from alvos.models.alvo import Alvo
from datetime import datetime

class AlvoModelTestCase(TestCase):
    def setUp(self):
        self.alvo = Alvo.objects.create(
            identificador="alvo001",
            nome="Alvo de Teste",
            latitude=-23.5,
            longitude=-46.6,
            data_expiracao="2025-12-31T23:59:59Z"
        )

    def test_criacao_de_alvo(self):
        self.assertEqual(self.alvo.nome, "Alvo de Teste")
