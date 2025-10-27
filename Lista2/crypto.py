import ecdsa
import hashlib

# funkcja do podpisywania wiadomosci
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
