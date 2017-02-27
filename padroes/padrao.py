import sys


try:
	file = open(sys.argv[1], 'rb')
	file_padrao = open('outputs/padrao_out.txt','wb')
except:
	print("Leia o Readme")

words = file.readlines()

patterns = {}
	
for x in words:
	x = x.replace("\n","")
	count = 0
	p = ''
	p_word = {}

	for i in x:
		if count == 0:	
			p_word.update({i: count})
			p += str(count)
			count += 1
		else:
			if p_word.get(i) == None:
				p_word.update({i: count})
				p += str(count)
				count += 1
			else:
				p += str(p_word.get(i))
	if x != p:
		patterns.update({x: p})
file_padrao.write(str(patterns))
