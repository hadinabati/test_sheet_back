import hashlib


def hash_password(password : str):
    md5 = hashlib.md5(password.encode())
    return md5.hexdigest()
