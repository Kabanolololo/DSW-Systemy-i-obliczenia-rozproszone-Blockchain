import json
import hashlib

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
