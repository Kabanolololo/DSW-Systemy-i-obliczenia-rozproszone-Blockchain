from crypto import sign_message

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
