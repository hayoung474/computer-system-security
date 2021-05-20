from Crypto.PublicKey import RSA

# Alice Side ( Key generation )
AlicePrivKey = RSA.generate(2048)
f = open("AlicePrivKey.pem",'wb')
# PEM is text and binary format
f.write(AlicePrivKey.export_key('PEM',passphrase="!@#$"))
f.close()
f=open("AlicePubKey.pem","wb")
f.write(AlicePrivKey.public_key().export_key('PEM'))
f.close()

