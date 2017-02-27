from Crypto import Random
from Crypto.PublicKey import RSA

random_generator = Random.new().read

key = RSA.generate(1024, random_generator)

public_key = key.publickey()

encry = public_key.encrypt('UNIVERSIDADE FEDERAL FRONTEIRA SUL' , 32)

print'\n encrypt \n ' + str(encry)

decry = key.decrypt(encry)

print '\n decrypt \n ' + str(decry)
