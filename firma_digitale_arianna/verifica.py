import hashlib  # Libreria per l'hashing (SHA256)
import rsa  # Libreria per la crittografia RSA
import os  # Libreria per controllare l'esistenza dei file

def main():
    # Controlla se il file della chiave privata esiste
    with open('private.txt', 'r') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read().encode('utf-8'))

    # Carica la stringa cifrata dal file
    with open('encrypted.txt', 'rb') as f:  # Legge il file in modalità binaria
        encrypted_string = f.read()

    # Carica la stringa originale dal file
    with open('testo_chiaro.txt', 'r') as f:
        input_string = f.read()

    # Calcola l'hash della stringa originale
    input_string_hash = hashlib.sha256(input_string.encode('utf-8')).hexdigest()

    # Decifra la stringa con la chiave privata
    decrypted_string = rsa.decrypt(encrypted_string, privkey)
    decrypted_string_hash = hashlib.sha256(decrypted_string).hexdigest()

    print("Stringa decifrata: ", decrypted_string.decode('utf-8'))

    # Controlla se la stringa iniziale e quella decifrata sono uguali
    if input_string_hash == decrypted_string_hash:
        print("La stringa iniziale e quella decifrata sono uguali")
    else:
        print("La stringa iniziale e quella decifrata non sono uguali")

if __name__ == "__main__":
    main()