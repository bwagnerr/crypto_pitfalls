import os
import hmac
from hashlib import sha256
from pycryptopp.cipher.aes import AES

plain_text = "Text to be encrypted"
secret_key = "* super secret key of 32 bytes *"
iv = os.urandom(16)

cipher_text = AES(key=secret_key, iv=iv).process(plain_text)
text_hmac = hmac.new(secret_key, ''.join((iv, cipher_text)), sha256).digest()
cipher_text = ''.join((text_hmac, cipher_text))

with open('file3', 'w') as file:
  file.write(cipher_text)
