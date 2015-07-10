#Problema: Persistir alguns dados em disco de forma segura

Possível solução:

Escolher alguma biblioteca de criptografia para criptografar os dados antes de salvar em disco e descriptografá-los ao carregar


#Primeira tentativa:

```python
from pycryptopp.cipher.aes import AES

plain_text = "Text to be encrypted"
secret_key = "* super secret key of 32 bytes *"
cipher_text = AES(key=secret_key).process(plain_text)

with open('file') as file:
  file.write(cipher_text)
```
Funciona! Temos uma solução, mas o que não vemos?

##IV (Initialization Vector)

Por não usarmos um IV aleatório, se alguém conseguir acesso a conteúdos cifrados é possível encontrar a relação entre os diferentes segmentos do texto criptografado e criar um dicionário para decifrar novos conteúdos

Exemplos: WEP (IV não era único), SSL 2.0 (IV era derivado da última mensagem e não aleatório)

#Segunda tentativa:

```python
import os
from pycryptopp.cipher.aes import AES

plain_text = "Text to be encrypted"
secret_key = "* super secret key of 32 bytes *"
iv = os.urandom(16)
cipher_text = AES(key=secret_key, iv=iv).process(plain_text)

with open('file') as file:
  file.write(cipher_text)
```

Funciona! E evitamos os problemas derivação, mas o que não vemos?

##HMAC (Hash-based message authentication code)

Melhoramos a solução para melhorar a privacidade, mas há outro problema, como garantir que o conteúdo que estou decifrando foi realmente cifrado por mim? Usando HMAC, conseguimos ter mais certeza de que o que estamos tentando decifrar não foi alterado e que realmente foi cifrado por mim.

#Terceira tentativa:

```python
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
```


# Alternativas:

Se você não tem tempo pra aprender criptografia, procure uma biblioteca de criptografia de alto nível pra fazer isso pra você.

Python:
[Cryptography](https://cryptography.io/en/latest/)
[NaCl](https://pynacl.readthedocs.org/en/latest/)

C e linguagens que usam extensões C:
[libnacl](http://nacl.cr.yp.to/)

Procure uma na sua linguagem!


#Obrigado!
