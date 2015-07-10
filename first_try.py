from pycryptopp.cipher.aes import AES

plain_text = "Text to be encrypted"
secret_key = "* super secret key of 32 bytes *"
cipher_text = AES(key=secret_key).process(plain_text)

with open('file1', 'w') as file:
  file.write(cipher_text)
