from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import pickle

# Alice Side ( send message )
f = open("AlicePrivKey.pem",'r')
AlicePrivKey = RSA.import_key(f.read(),passphrase="!@#$")
f.close()

message = "To be signed"
h  = SHA256.new(message.encode("utf-8"))
signature = pkcs1_15.new(AlicePrivKey).sign(h)

data = {'message':message, 'signature': signature}

# save data
with open('send_data.pickle','wb') as fw:
    pickle.dump(data, fw)

print("Alice sent(",message,signature,") to Bob.")
