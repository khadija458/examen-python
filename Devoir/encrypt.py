from base64 import b64encode, b64decode

def chiffrer_tel(tel):
    return b64encode(tel.encode()).decode()

def dechiffrer_tel(tel_chiffre):
    return b64decode(tel_chiffre.encode()).decode()
