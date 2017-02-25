from Crypto.Cipher 		import AES
from Crypto 			import Random

data = "UNIVERSIDADE FEDERAL FRONTEIRA SUL"
key = "A1b2c3D4567890123498760123456789"

IV = Random.new().read(AES.block_size)


cipher = AES.new(key, mode=AES.MODE_CFB, IV=IV)

encry = IV + cipher.encrypt(data)
decry = cipher.decrypt(encry)


print '\n encrypt \n ' + str(encry)
print '\n decrypt \n ' + str(decry[AES.block_size:])