import json
import hashlib
import datetime

# Klasa Blok
class Block:
    def __init__(self, index, date, data, previous_hash, nonce=0):
        self.index = index
        self.date = date
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    # Metoda tworzaca hash
    def calculate_hash(self):
        block_content = {
            'index': self.index,
            'date': self.date,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }
        json_data = json.dumps(block_content, sort_keys=True)
        created_hash = hashlib.sha256(json_data.encode())
        return created_hash.hexdigest()

    # Metoda kopania bloków
    def mine_block(self, difficulty):
        target = "0" * int(difficulty)
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()

# Klasa Blokchain
class Blockchain:
    def __init__(self):
        self.blocks = []
        self.pending_transactions = []

    # Metoda do tworzenia bloku poczatkowego
    def add_genesis_block(self):
        block = Block(index=0, date=str(datetime.datetime.now().timestamp()), data='created by python', previous_hash=0)
        self.blocks.append(block)

    # Metoda do pobrania wczesniejszego bloku
    def get_previous_block(self):
        return self.blocks[-1]

    # Metoda do dodawnia bloku
    def add_block(self, difficulty = 3):
        previous_block = self.get_previous_block()

        new_index = previous_block.index + 1
        new_date = str(datetime.datetime.now().timestamp())
        previous_hash = previous_block.hash

        # Dodanie nowego bloku
        block = Block(new_index, new_date,self.pending_transactions,  previous_hash)
        
        # Kopanie bloku
        block.mine_block(difficulty)
        self.blocks.append(block)
        
        # Czystka buforu
        self.pending_transactions = []

    # Metoda do walidacji hashy
    def is_chain_valid(self):
        for x in range(1, len(self.blocks)):
            previous_hash = self.blocks[x].previous_hash
            previous_block_hash = self.blocks[x - 1].hash

            if previous_hash != previous_block_hash:
                print(f"Blok {x} ma niepoprawny hash poprzedniego bloku!")
                return False

        print("Hashes are valid.")
        return True
    
    # Metoda dodawania transakcji
    def add_transaction(self, sender, receiver, amount):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        self.pending_transactions.append(transaction)

# Inicjalizacja blockchaina
my_blockchain = Blockchain()

# Dodanie bloku początkowego (genesis block)
my_blockchain.add_genesis_block()

########################### PRZYKLADOWE BLOKI I TRAKNSAKCJE WYGENEROWANE PRZEZ CHATGPT ###########################
# 🔹 BLOK 1
my_blockchain.add_transaction("Alicja", "Bob", 10)
my_blockchain.add_transaction("Bob", "Ewa", 5)
my_blockchain.add_transaction("Ewa", "Alicja", 2)
my_blockchain.add_transaction("Karol", "Marta", 3)
my_blockchain.add_transaction("Marta", "Tomek", 1)
my_blockchain.add_block()  # Tworzymy blok z powyższymi transakcjami

# 🔹 BLOK 2
my_blockchain.add_transaction("Tomek", "Alicja", 4)
my_blockchain.add_transaction("Ewa", "Karol", 2)
my_blockchain.add_transaction("Alicja", "Ewa", 6)
my_blockchain.add_transaction("Marta", "Bob", 5)
my_blockchain.add_block()  # Drugi blok

# 🔹 BLOK 3
my_blockchain.add_transaction("Bob", "Karol", 7)
my_blockchain.add_transaction("Karol", "Ewa", 1)
my_blockchain.add_transaction("Ewa", "Alicja", 3)
my_blockchain.add_transaction("Tomek", "Marta", 8)
my_blockchain.add_transaction("Alicja", "Tomek", 2)
my_blockchain.add_block()  # Trzeci blok

# 🔹 BLOK 4
my_blockchain.add_transaction("Marta", "Ewa", 10)
my_blockchain.add_transaction("Ewa", "Karol", 2)
my_blockchain.add_transaction("Tomek", "Bob", 1)
my_blockchain.add_transaction("Alicja", "Marta", 7)
my_blockchain.add_block()  # Czwarty blok

# Wypisanie bloków i ich hashy
for block in my_blockchain.blocks:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.date}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 60)

# Walidacja bloków
my_blockchain.is_chain_valid()
