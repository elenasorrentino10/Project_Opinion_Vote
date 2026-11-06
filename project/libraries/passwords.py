import base64
import hashlib
import hmac
import os

SCHEME = 'scrypt'
SCRYPT_PARAMS = {'n': 2 ** 14, 'r': 8, 'p': 1}


def _derive(password: str, salt: bytes) -> bytes:
    return hashlib.scrypt(password.encode(), salt=salt, **SCRYPT_PARAMS)


def hash_password(password: str) -> str:
    """Return a salted hash that is safe to store in the database."""
    salt = os.urandom(16)
    encoded_salt = base64.b64encode(salt).decode()
    encoded_digest = base64.b64encode(_derive(password, salt)).decode()
    return f'{SCHEME}${encoded_salt}${encoded_digest}'


def verify_password(password: str, stored: str) -> bool:
    """Check a password against a value created by hash_password."""
    try:
        scheme, encoded_salt, encoded_digest = stored.split('$')
        salt = base64.b64decode(encoded_salt, validate=True)
        digest = base64.b64decode(encoded_digest, validate=True)
    except ValueError:
        return False

    if scheme != SCHEME:
        return False

    return hmac.compare_digest(_derive(password, salt), digest)
