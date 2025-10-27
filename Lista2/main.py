import os
import ecdsa 
import hashlib

# funkcja do stworzenia portfela
def create_wallet():

    # generowanie klucza prywatnego
    def generate_private_key():
        private_key = os.urandom(32).hex()
        return private_key

    # generowanie klucza publicznego
    def generate_public_key(private_key):

        # konwersja z hexa na bytes
        private_key_bytes = bytes.fromhex(private_key)

        # tworzenie klucza na krzywej
        sign_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)

        # uzyskanie klucza
        verify_key = sign_key.verifying_key

        # pobranie wspolrzednych X Y
        public_key_bytes = verify_key.to_string()
        x = public_key_bytes[:32]
        y = public_key_bytes[32:]

        # sprawdzenie parzystosci Y
        y_int = int.from_bytes(y, byteorder='big')
        if y_int % 2 == 0:
            #print("Y jest parzysta")
            prefix = b'\x02'
        else:
            #print("Y jest nieparzysta")
            prefix = b'\x03'

        # stworzenie skompresowanego klucza
        compressed_public_key = prefix + x

        # generowanie adresu blockchain
        def generate_blockchain_address(compressed_public_key):

            # haszowanie klucza publicznego SHA-256
            sha256_public_key = hashlib.sha256(compressed_public_key).digest()

            # haszowanie na RIPMED-160
            ripemd160 = hashlib.new('ripemd160')
            ripemd160.update(sha256_public_key)

            public_key_hash = ripemd160.digest()

            return public_key_hash

        # zwracanie wartosci
        compressed_public_key_hex = compressed_public_key.hex()
        public_key_hash = generate_blockchain_address(compressed_public_key)
        blockchain_address_hex = public_key_hash.hex()
        return compressed_public_key_hex, blockchain_address_hex

    # generowanie prywatnego klucza
    private_key = generate_private_key()

    # generowanie publicznego klucza i adresu
    public_key, address = generate_public_key(private_key)

    # zwracanie wszystkiego jako slownik
    return {
        "private_key": private_key,
        "public_key": public_key,
        "address": address
    }

# funkcja do podpisywania i weryfikacji wiadomosci
def sign_message(private_key_hex, message):
    
    # konwersja klucza prywatnego z hexa na bytes
    private_key_bytes = bytes.fromhex(private_key_hex)
    
    # tworzenie klucza na krzywej
    sign_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
    
    # hashowanie wiadomosci 
    message_bytes = message.encode('utf-8')
    message_hash = hashlib.sha256(message_bytes).digest()
    
    # podpis ECDSA
    signature = sign_key.sign_digest(message_hash)
    
    # konwersja podpisu na hex
    signature_hex = signature.hex()
    
    return signature_hex


if __name__ == "__main__":
    wallet = create_wallet()
    print("Wygenerowany wallet:", wallet)
    private_key = wallet["private_key"]

    message = "Przelew 1 BTC do Alice"

    # podpisanie wiadomości
    signature = sign_message(private_key, message)
    print("Podpis (hex):", signature)