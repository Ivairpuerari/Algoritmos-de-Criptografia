import Crypto
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import hashlib
import sys

if sys.argv[1] == 'assinatura':
	doc = open(sys.argv[2], 'r+')
	h = hashlib.sha256()
	buff = doc.read()
	h.update(buff.encode('UTF-8'))
	has = h.hexdigest()
	
	random_generator =  Random.new().read
	
	key = RSA.generate(1024, random_generator)
	public_Key = key.publickey()

	encry = public_Key.encrypt(has.encode(encoding = 'UTF-8'), 32)

	file_out = open('certi_out','w')

	file_out.write(has +'\n')
	
	file_out.write(str(encry) + '\n')
	file_out.write(str(public_Key.exportKey('PEM').decode('UTF-8')))
	file_out.close()

if sys.argv[1] == 'verifica':

	doc_v = open(sys.argv[3]).read()
	file_in = doc_v.split('\n')
	
	hash_v = file_in[0]

	doc = open(sys.argv[2], 'r+')
	h = hashlib.sha256()
	buff = doc.read()
	h.update(buff.encode('UTF-8'))
	has = h.hexdigest()
	
	if(has == hash_v):
		print ('Assinatura compativel')
	else:
		print ('Assinatura imcompativel com o documento')
