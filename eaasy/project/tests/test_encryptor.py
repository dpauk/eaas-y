import pytest

from project.tests.base import BaseTestCase
from project.encryptor import Encryptor


class TestEncryptor(BaseTestCase):
    def test_encryptor_doesnt_return_nothing_when_passed_a_string(self):
        encryptor = Encryptor()
        plaintext = "Hello, I'm a string to encrypt."
        assert encryptor.encrypt(plaintext) != ""

    def test_encryptor_returns_different_string(self):
        """The basic case is that the object has a string
        pushed and returns something different."""
        encryptor = Encryptor()
        plaintext = "Hello, I'm a string to encrypt."
        assert encryptor.encrypt(plaintext) != plaintext

    def test_encryptor_returns_an_exception_with_an_empty_value(self):
        encryptor = Encryptor()
        with pytest.raises(ValueError):
            encryptor.encrypt("")

    def test_encryptor_returns_an_exception_with_a_none_value(self):
        encryptor = Encryptor()
        with pytest.raises(ValueError):
            encryptor.encrypt(None)

    def test_encryptor_returns_an_exception_if_value_not_a_string(self):
        encryptor = Encryptor()
        with pytest.raises(ValueError):
            encryptor.encrypt(67)


if __name__ == '__main__':
    pytest.main()
