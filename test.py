

def  dec2bin(n=int(0)):
	result = []

	while n > 0:
		rest = n%2
		n//=2

		result.append(str(rest))

	result.reverse()
	return "".join(result)



def  bin2dec(n="0"):
	c, result = len(n)-1,0
	for i in range(len(n)):
		result += int(n[i]) * 2**c

		c-=1

	return result



def dec2hexa(n=int(0)):
	result = []
	m = {
		"A":10,
		"B":11,
		"C":12,
		"D":13,
		"E":14,
		"F":15
	}

	c = n 
	while c > 0:
		rest = c%16
		c //= 16
		
		result.append(rest)

	result.reverse()

	for i in range(len(result)):

		for k,v in m.items():
			if result[i] == v:
				result[i] = k


	return result



def hexa2dec(l=[]):
	m = {
		"A":10,
		"B":11,
		"C":12,
		"D":13,
		"E":14,
		"F":15
	}
	result = 0

	for i in range(len(l)):
		if l[i] in list(m.keys()):
			l[i] = m[l[i]] 

	p = len(l)-1
	for i in l:

		result += i*(16**p)
		p-=1

	return result


	
def bin2hex(l=[])
	result = ""

	for i in l:
		


#main
x = bin2hex(["F","F","F"])
print(x)
