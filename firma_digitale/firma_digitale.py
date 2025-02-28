from hashlib import sha256
from rsa_python import rsa

testo_chiaro=input("Inserisci il testo in chiaro: \n")
testo_sha=sha256(testo_chiaro.encode('utf-8')).hexdigest()
print(testo_sha)
key_pair = rsa.generate_key_pair(1024)
cifrato= rsa.encrypt(testo_sha,key_pair["private"], key_pair["modulus"])
#decrypted_message = rsa.decrypt(cifrato, key_pair["public"], key_pair["modulus"])
print(cifrato)
