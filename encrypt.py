from Crypto.Cipher import AES
from Crypto.Util import Counter
import binascii

key = b"GALOIS_1811_1832"
nonce = b"2026CTF!"

messages = [
    b"Lettre de Galois a Auguste Chevalier, 1832.\n",
    b"An author never does more damage to his readers than when he hides a difficulty.\n",
    b"Tu y es presque, le flag est : FLAG{d6a7906a0450158d0682d1a96d48de28}\n"
]

def encrypt(plaintext):
    ctr = Counter.new(64, prefix=nonce)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(plaintext)

for i, msg in enumerate(messages):
    c = encrypt(msg)
    print(f'c{i+1} = bytes.fromhex("{binascii.hexlify(c).decode()}")')