import rsa

(kpub, kpriv) = rsa.newkeys(512)
print("Key:", kpub, kpriv)

crypto = rsa.encrypt('hello Python'.encode('utf-8'), kpub)
print(crypto)

message = rsa.decrypt(crypto, kpriv)
print(message.decode('utf8'))
