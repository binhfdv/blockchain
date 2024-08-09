from Crypto.Hash import RIPEMD160
from hashlib import sha256

def hash256(s):
    return sha256(sha256(s).digest()).digest()

def hash160(s):
    return RIPEMD160.new(sha256(s).digest()).digest()