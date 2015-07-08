import os
import hmac
from pycryptopp.cipher.aes import AES

plain_text = "Text to be encrypted"
secret_key = "* super secret key of 32 bytes *"
iv = os.urandom(16)
cipher_text = AES(key=secret_key, iv=iv).process(plain_text)
<hmac example here>

with open('file') as file:
  file.write(cipher_text)
