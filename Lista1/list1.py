import json
import hashlib

# Klasa Blok
class Block:
    def __init__(self, index, date, data, previous_hash):
        self.index = index
        self.date = date
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Metoda ktora tworzy SHA-256 z połączenia index, timestamp, data, previous_hash.
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