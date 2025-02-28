import hashlib  # Libreria per l'hashing (SHA256)
import rsa  # Libreria per la crittografia RSA
import os  # Libreria per controllare l'esistenza dei file

def main():
    # Controlla se i file delle chiavi esistono
    if os.path.exists('private.txt') and os.path.exists('public.txt'):
        # Carica le chiavi dai file
        with open('private.txt', 'r') as f:
            privkey = rsa.PrivateKey.load_pkcs1(f.read().encode('utf-8'))

        with open('public.txt', 'r') as f:
            pubkey = rsa.PublicKey.load_pkcs1(f.read().encode('utf-8'))
    else:
        # Genera chiavi pubbliche e private
        pubkey, privkey = rsa.newkeys(512)

        # Salva le chiavi in file di testo
        with open('private.txt', 'w') as f:
            f.write(privkey.save_pkcs1().decode('utf-8'))  # Scrive la chiave privata nel file in formato stringa

        with open('public.txt', 'w') as f:
            f.write(pubkey.save_pkcs1().decode('utf-8'))  # Scrive la chiave pubblica nel file in formato stringa

    # Inserisco la stringa da cifrare
    input_string = input("Inserisci la stringa da cifrare: ") 
    with open('testo_chiaro.txt', 'w') as f:
        f.write(input_string)

    encoded_string = input_string.encode('utf-8')  # Trasformo la stringa in binario

    # Hash della stringa inserita
    hashed_string = hashlib.sha256(encoded_string).hexdigest()
    print("Hash della stringa inserita: ", hashed_string)

    # Cifro la stringa con la chiave pubblica
    encrypted_string = rsa.encrypt(encoded_string, pubkey)
    print("Stringa cifrata: ", encrypted_string)
    #creo il file dove salvare la stringa cifrata
    with open('encrypted.txt', 'w') as f:
        f.write(str(encrypted_string))

if __name__ == "__main__":
    main()