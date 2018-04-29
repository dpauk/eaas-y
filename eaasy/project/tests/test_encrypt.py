import json

from project.tests.base import BaseTestCase


class TestEncryptService(BaseTestCase):
    def test_encrypt_returns_a_value(self):
        """Ensure the api can call the encryptor properly"""
        with self.client:
            plaintext = "Hello, I'm a string to encrypt."
            response = self.client.get("/encrypt/{plaintext}")
            data = json.loads(response.data.decode())
            assert response.status_code == 200
            assert data['data']['ciphertext'] != plaintext

    # def test_ping(self):
    #     with self.client:
    #         response = self.client.get('/encrypt/ping')
    #         assert response.status_code == 200
