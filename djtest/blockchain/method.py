import hashlib
def hash(data):
    return hashlib.sha256(data).hexdigest()