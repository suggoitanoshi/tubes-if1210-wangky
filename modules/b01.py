#F01 - HASH PASSWORD

#KAMUS

import hashlib

def hashpassword(password):
    m = hashlib.sha256(password.encode())
    return m.hexdigest()

def verify(passinput,passhashed):
    if(hashpassword(passinput)==passhashed):
        return True
    return False
