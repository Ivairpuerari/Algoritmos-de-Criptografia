from sys import argv


alice = 0
ac = 0
bob = 0
bc = 0
N = 179424673
base = 17

def calcKey(  chave,  base,  mod) :
	return (base**chave) % mod

if argv[1] == 'alice':
	alice = int(argv[2])
	ac = calcKey(alice, base, N)
	print 'chave intermediaria: '+ str(ac) 
if argv[3] == 'bob':
	bob = int(argv[4])
	bc = calcKey(bob, base, N)
	print 'chave intermediaria: '+ str(bc) 

print 'chave compartilhada por alice: ' + str(calcKey(alice, bc, N));
print 'chave compartilhada por bob: ' + str(calcKey(bob, ac, N));
