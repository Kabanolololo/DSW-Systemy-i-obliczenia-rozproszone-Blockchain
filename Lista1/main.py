from blockchain import Blockchain

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

# Symulacja zmiany transakcji w bloku 2 (atak / błąd)
# my_blockchain.blocks[2].data[0]["amount"] = 999

# Wypisanie bloków i ich hashy
for block in my_blockchain.blocks:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.date}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 60)

# Walidacja blockchaina z raportem błędów
valid, errors = my_blockchain.is_chain_valid()
