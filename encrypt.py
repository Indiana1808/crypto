#!/usr/bin/python3

#creation d'un scouple
from Crypto.PublicKey import RSA

#creation d'un couple de clés, publique et prive sont tous dedans 
key = RSA.generate(1024)

#chiffrage
public_key = key.publickey()
f= open('test1.txt', 'r')
contenu = f.read()
f.close()
enc_data = public_key.encrypt(test1.txt)

#ecriture dans un nouveaux fichier
f= open('test1.txt', 'wb')
texte = f.write(enc_data[0])
f.close()
enc_data = public_key.encrypt(test1.txt)



#afficher ses clés 
k = key.exportKey('PEM')
p = key.publickey().exportKey('PEM')


#sauvegarder le clé
with open('private.pem','w') as kf:
	kf.write(k.decode())
	kf.close()

with open('public.pem','w') as pf:
	pf.write(p.decode())
	pf.close()

privat = RSA.importKey(priv)
public = RSA.importKey(pub)

print(enc_data)


