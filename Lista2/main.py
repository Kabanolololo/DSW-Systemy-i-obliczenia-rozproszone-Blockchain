from wallet import create_wallet
from crypto import sign_message, verify_signature
from transaction import create_transaction
from blockchain import blockchain, add_transaction, save_blockchain, load_blockchain

if __name__ == "__main__":

    # wczytanie blockchaina z pliku
    load_blockchain()

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

        # podpisujemy wiadomosc dla tej transakcji
        message = f"{tx['sender']}->{tx['recipient']}:{tx['amount']}"
        signature = sign_message(info["sender_wallet"]["private_key"], message)
        tx["signature"] = signature

        # weryfikacja podpisu
        valid = verify_signature(info["sender_wallet"]["public_key"], message, signature)
        print(f"Transakcja {len(blockchain)+1}, podpis poprawny?", valid)

        # dodanie do blockchaina z unikalnym ID
        tx_block = add_transaction(tx)
        print(f"Dodano transakcje do blockchaina: {tx_block}")

    # zapis blockchaina do pliku JSON
    save_blockchain()
    print("Blockchain zapisany do pliku blockchain.json")

    # wyswietlenie calego blockchaina
    print("Aktualny blockchain:", blockchain)
