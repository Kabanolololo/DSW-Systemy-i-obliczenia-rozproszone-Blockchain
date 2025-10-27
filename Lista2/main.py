import os
import ecdsa 
import hashlib
import json

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

# funkcja weryfikujaca podpis publicznym kluczem
def verify_signature(public_key_hex, message, signature_hex):
    
    # konwersja public key z hex na bytes
    public_key_bytes = bytes.fromhex(public_key_hex)

    # jesli 33 bajty, rozpakowujemy do 64 bajty
    if len(public_key_bytes) == 33:
        prefix = public_key_bytes[0]
        x_bytes = public_key_bytes[1:]
        x = int.from_bytes(x_bytes, 'big')

        # secp256k1 prime
        p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F

        # obliczamy y^2 = x^3 + 7 mod p
        y2 = (pow(x, 3, p) + 7) % p
        y = pow(y2, (p + 1)//4, p)

        # wybieramy y o dobrej parzystosci
        if (y % 2 == 0 and prefix == 3) or (y % 2 == 1 and prefix == 2):
            y = p - y

        y_bytes = y.to_bytes(32, 'big')
        uncompressed_pubkey_bytes = x_bytes + y_bytes  # 64 bajty
    elif len(public_key_bytes) == 64:
        uncompressed_pubkey_bytes = public_key_bytes
    else:
        raise ValueError("Nieprawidlowy format klucza publicznego")

    # tworzymy verifyingkey z surowych wspolrzednych xy
    verify_key = ecdsa.VerifyingKey.from_string(uncompressed_pubkey_bytes, curve=ecdsa.SECP256k1)

    # hashujemy wiadomosc SHA-256
    message_bytes = message.encode()
    message_hash = hashlib.sha256(message_bytes).digest()

    # konwersja podpisu z hex na bytes
    signature_bytes = bytes.fromhex(signature_hex)

    # weryfikacja podpisu
    try:
        valid = verify_key.verify_digest(signature_bytes, message_hash)
        return valid
    except ecdsa.BadSignatureError:
        return False

# funkcja do tworzenia transakcji
def create_transaction(sender_wallet, recipient_address, amount):

    # tworzymy wiadomosc transakcji jako string
    message = f"{sender_wallet['address']}->{recipient_address}:{amount}"

    # podpisujemy wiadomosc prywatnym kluczem nadawcy
    signature = sign_message(sender_wallet['private_key'], message)

    # tworzymy slownik transakcji
    transaction = {
        "sender": sender_wallet['address'],
        "recipient": recipient_address,
        "amount": amount,
        "signature": signature
    }

    return transaction

# funkcja dodajaca transakcje do "blockchaina"
def add_transaction_to_blockchain(transaction):
    # przypisanie unikalnego ID (liczba kolejna)
    tx_id = len(blockchain) + 1
    transaction_block = {
        "id": tx_id,
        "sender": transaction["sender"],
        "recipient": transaction["recipient"],
        "amount": transaction["amount"],
        "signature": transaction["signature"]
    }
    blockchain.append(transaction_block)
    return transaction_block

# funkcja zapisujaca blockchain do pliku JSON
def save_blockchain_to_file(filename="blockchain.json"):
    with open(filename, "w") as f:
        json.dump(blockchain, f, indent=4)

# funkcja wczytujaca blockchain z pliku JSON
def load_blockchain_from_file(filename="blockchain.json"):
    global blockchain
    try:
        with open(filename, "r") as f:
            blockchain = json.load(f)
    except FileNotFoundError:
        blockchain = []
        
        
if __name__ == "__main__":
    import json

    # lista symulujaca blockchain
    blockchain = []

    # generujemy portfele nadawcow
    sender_wallet1 = create_wallet()
    sender_wallet2 = create_wallet()
    print("Wygenerowane portfele:")
    print("Wallet 1:", sender_wallet1)
    print("Wallet 2:", sender_wallet2)

    # lista przykładowych transakcji do dodania
    transactions_info = [
        {"sender_wallet": sender_wallet1, "recipient": "1RecipientAddressA", "amount": 0.5},
        {"sender_wallet": sender_wallet1, "recipient": "1RecipientAddressB", "amount": 1.2},
        {"sender_wallet": sender_wallet2, "recipient": "1RecipientAddressC", "amount": 2.0},
        {"sender_wallet": sender_wallet2, "recipient": "1RecipientAddressD", "amount": 0.75},
    ]

    # tworzymy i dodajemy transakcje do blockchaina
    for info in transactions_info:
        # tworzymy transakcje
        tx = create_transaction(info["sender_wallet"], info["recipient"], info["amount"])
        
        # podpisujemy wiadomość dla tej transakcji
        message = f"{tx['sender']}->{tx['recipient']}:{tx['amount']}"
        signature = sign_message(info["sender_wallet"]["private_key"], message)
        tx["signature"] = signature

        # weryfikacja podpisu
        valid = verify_signature(info["sender_wallet"]["public_key"], message, signature)
        print(f"Transakcja {len(blockchain)+1}, podpis poprawny?", valid)

        # dodanie do blockchaina z unikalnym ID
        tx_block = {
            "id": len(blockchain) + 1,
            "sender": tx["sender"],
            "recipient": tx["recipient"],
            "amount": tx["amount"],
            "signature": tx["signature"]
        }
        blockchain.append(tx_block)
        print(f"Dodano transakcje do blockchaina: {tx_block}")

    # zapis blockchaina do pliku JSON
    with open("blockchain.json", "w") as f:
        json.dump(blockchain, f, indent=4)
    print("Blockchain zapisany do pliku blockchain.json")

    # wyswietlenie calego blockchaina
    print("Aktualny blockchain:", blockchain)
