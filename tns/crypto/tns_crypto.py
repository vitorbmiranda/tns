import os, base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

encrypter = None


def init(key_location):
    """
    Sets up our crypto library
    """

    global encrypter

    key = __load_key(key_location)

    # have to use some shenanigans to generate a custom key
    # https://github.com/pyca/cryptography/issues/1333

    backend = default_backend()
    salt = os.urandom(16)

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=backend
    )

    final_key = base64.urlsafe_b64encode(kdf.derive(key.encode()))

    encrypter = Fernet(final_key)


def encrypt(text):
    return encrypter.encrypt(text.encode())


def decrypt(text):
    return encrypter.decrypt(text).decode("UTF-8")


def __load_key(key_location):

    with open(key_location, 'r') as keyfile:
        key = keyfile.read()

    return key
