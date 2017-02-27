import sys


def ceaserE(file, key, doc_cifrado) :	
	for i in file:
	  cifra = (int((ord(i) + key) % 256))
	  doc_cifrado.write(chr(cifra))
	print ("Cifrado.")	
def ceaserD(doc_decifrado, key, doc_cifrado) :	
	for i in doc_cifrado:
	  cifra = (int((ord(i) - key) % 256))
	  doc_decifrado.write(chr(cifra))
	print ("Descifrado.")	

try:
	Nfile = open(sys.argv[2],'rb');
	key = int(sys.argv[3])
	
except:
	print('Leia o readme e execute novamente!')

if sys.argv[1] == 'cifrar' :
	
	file = Nfile.read()
	doc_cifrado = open('outputs/cifrado_de_ceazar','wb')

	ceaserE(file, key, doc_cifrado)

if sys.argv[1] == 'decifrar' :

	doc_cifrado = open('outputs/cifrado_de_ceazar').read()
	doc_decifrado = open('outputs/decifrado_de_ceazar','wb')

	ceaserD(doc_decifrado, key, doc_cifrado)
