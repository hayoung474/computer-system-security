from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import pickle

# Bob side ( receive message )

f = open("AlicePubKey.pem",'r')
AlicePubKey = RSA.import_key(f.read())
f.close()

message=""
signature=""
with open('send_data.pickle', 'rb') as fr:
    data = pickle.load(fr)
    message=data['message']
    signature = data['signature']

print("Bob received message (",message,signature,") from Alice")
h = SHA256.new(message.encode('utf-8'))

try:
    pkcs1_15.new(AlicePubKey).verify(h,signature)
    print("The signature is valid")
except(ValueError , TypeError):
    print("The signature is not valid")