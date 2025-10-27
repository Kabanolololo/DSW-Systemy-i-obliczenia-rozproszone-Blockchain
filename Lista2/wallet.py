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
        sha256_public_key = hashlib.sha256(compressed_public_key).digest()
        ripemd160 = hashlib.new('ripemd160')
        ripemd160.update(sha256_public_key)
        blockchain_address_hex = ripemd160.digest().hex()

        return compressed_public_key.hex(), blockchain_address_hex

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
