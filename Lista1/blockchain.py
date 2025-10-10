from block import Block
import datetime

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

    # Metoda dodawania transakcji
    def add_transaction(self, sender, receiver, amount):
        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        }
        self.pending_transactions.append(transaction)

    # Rozszerzona metoda walidacji blockchaina (zad 7)
    def is_chain_valid(self, difficulty=3):
        errors = []

        # Sprawdzenie dlugosci bloku
        if len(self.blocks) < 1:
            errors.append("Blockchain jest pusty")

        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]

            # Sprawdzenie czy hash bloku jest poprawny
            if current_block.hash != current_block.calculate_hash():
                errors.append(f"Blok {i}: ma nieprawidlowy hash")

            # Sprawdzenie czy previous_hash zgadza się z poprzednim blokiem
            if current_block.previous_hash != previous_block.hash:
                errors.append(f"Blok {i}: previous_hash nie zgadza sie")

            # Sprawdzenie pow
            target = "0" * difficulty
            if not current_block.hash.startswith(target):
                errors.append(f"Blok {i}: Hash nie spelnia warunku proof-of-work")

        # Wypisywanie bledow
        if errors:
            print("Bledy w blockchainie:")
            for e in errors:
                print(" -", e)
            return False, errors
        else:
            print("Blockchain jest poprawny.")
            return True, []
