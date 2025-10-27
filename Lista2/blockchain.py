import json

# lista symulujaca blockchain
blockchain = []

# funkcja dodajaca transakcje do "blockchaina"
def add_transaction(transaction):
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
def save_blockchain(filename="blockchain.json"):
    with open(filename, "w") as f:
        json.dump(blockchain, f, indent=4)

# funkcja wczytujaca blockchain z pliku JSON
def load_blockchain(filename="blockchain.json"):
    global blockchain
    try:
        with open(filename, "r") as f:
            blockchain = json.load(f)
    except FileNotFoundError:
        blockchain = []
