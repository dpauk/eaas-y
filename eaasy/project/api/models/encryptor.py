import os

from cryptography.fernet import Fernet


class Encryptor:
    def encrypt(self, plaintext):
        if plaintext == "" or not isinstance(plaintext, str):
            raise ValueError
        key = bytes(os.environ["ENCRYPTION_KEY"], "utf-8").decode("unicode_escape")
        f = Fernet(key)
        return f.encrypt(bytes(plaintext, "utf-8")).decode("utf-8")
