import json
import hashlib
import datetime

# Klasa Blok
class Block:
    def __init__(self, index, date, data, previous_hash):
        self.index = index
        self.date = date
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Metoda tworzaca hash
    def calculate_hash(self):
        block_content = {
            'index': self.index,
            'date': self.date,
            'data': self.data,
            'previous_hash': self.previous_hash
        }
        json_data = json.dumps(block_content, sort_keys=True)
        created_hash = hashlib.sha256(json_data.encode())
        return created_hash.hexdigest()

# Klasa Blokchain
class Blockchain:
    def __init__(self):
        self.blocks = []

    # Metoda do tworzenia bloku poczatkowego
    def add_genesis_block(self):
        block = Block(index=0, date=str(datetime.datetime.now().timestamp()), data='created by python', previous_hash=0)
        self.blocks.append(block)

    # Metoda do pobrania wczesniejszego bloku
    def get_previous_block(self):
        return self.blocks[-1]

    # Metoda do dodawnia bloku
    def add_block(self, data):
        previous_block = self.get_previous_block()

        new_index = previous_block.index + 1
        new_date = str(datetime.datetime.now().timestamp())
        previous_hash = previous_block.hash

        block = Block(new_index, new_date, data, previous_hash)
        self.blocks.append(block)

# Inicjalizacja blockchaina
my_blockchain = Blockchain()

# Dodanie bloku początkowego
my_blockchain.add_genesis_block()

# Dodanie przykładowych bloków z danymi
my_blockchain.add_block("Transakcja: Alicja wysyła 10 BTC do Boba")
my_blockchain.add_block("Transakcja: Bob wysyła 5 BTC do Ewy")
my_blockchain.add_block("Transakcja: Ewa wysyła 2 BTC do Alicji")

# Wypisanie bloków i ich hashy
for block in my_blockchain.blocks:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.date}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 30)