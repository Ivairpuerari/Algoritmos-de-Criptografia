import sys
from itertools import cycle

def vigenereE(file, key, doc_cifrado) :
	for (a, b) in zip (cycle(key),file):
		cifra = (int((ord(b) + a) % 256))
		doc_cifrado.write(chr(cifra))
	
	print("Cifrado.")

def vigenereD(doc_cifrado, key, doc_decifrado) :
	for (a, b) in zip (cycle(key),doc_cifrado):
		cifra = (int((ord(b) - a) % 256))
		doc_decifrado.write(chr(cifra))
	
	print("Decifrado.")

def arrayKey(key):
	return (ord(i) for i in key)
try:
	Nfile = open(sys.argv[2],'rb');
	key = arrayKey(sys.argv[3])

except:
	print('Leia o readme e execute novamente!')

if sys.argv[1] == 'cifrar' :
	file = Nfile.read()
	doc_cifrado = open('outputs/cifrado_de_vig','wb')
	vigenereE(file, key, doc_cifrado)

if sys.argv[1] == 'decifrar' :

	doc_cifrado = open('outputs/cifrado_de_vig').read()
	doc_decifrado = open('outputs/decifrado_de_vig','wb')
	vigenereD(doc_cifrado, key, doc_decifrado)