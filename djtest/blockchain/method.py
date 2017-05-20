import hashlib
def hash(data):
    return hashlib.sha256(data).hexdigest()
def sha512(data):
    return hashlib.sha512(data).hexdigest()