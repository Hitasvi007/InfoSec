from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def generate_key_pair():
    key = RSA.generate(2048)  
    private_key = key.export_key()
    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(private_key)
    public_key = key.publickey().export_key()
    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(public_key)

def sign_file(file_to_sign, private_key_file, signature_file):
    with open(private_key_file, "rb") as key_file:
        private_key = RSA.import_key(key_file.read())
    with open(file_to_sign, "rb") as file:
        data = file.read()
    h = SHA256.new(data)
    signature = pkcs1_15.new(private_key).sign(h)
    with open(signature_file, "wb") as sig_file:
        sig_file.write(signature)

def verify_signature(file_to_verify, public_key_file, signature_file):
    with open(public_key_file, "rb") as key_file:
        public_key = RSA.import_key(key_file.read())
    with open(file_to_verify, "rb") as file:
        data = file.read()
    h = SHA256.new(data)
    with open(signature_file, "rb") as sig_file:
        signature = sig_file.read()
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is not valid.")

generate_key_pair()

sign_file("file_to_sign.txt", "private_key.pem", "signature.bin")

verify_signature("file_to_sign.txt", "public_key.pem", "signature.bin")
