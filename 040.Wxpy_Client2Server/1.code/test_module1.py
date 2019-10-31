import rsa
paw='ivan'
content=rsa.encrypt(paw,rsa.n,rsa.e)
print content
print len(content)
print rsa.decrypt(content,rsa.n,rsa.e,rsa.d)
print rsa.a()