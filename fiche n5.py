def points(mot):
	scrabble = {1:"A,E,I,L,N,O,R,S,T,U",
	2:"D,G,M",
	3:"B,C,P",5:"F,H,V",
	8:"J,Q",
	10:"K,W,X,Y,Z"}

	pcount = 0
	for char in mot:
		for point,chars in scrabble.items():
			if char.upper() in chars.split(","):  # True si le lettre se trouve dans ["A","B","C"] 
				pcount += point

	return pcount

	
def occurence(L):
	d = {}
	for i in L:
		if i in d:
			d[i] +=1

		else:
			d[i] = 1

	return d


def more_frecuent(d):
	result = d[list(d.keys())] [list(d.values()).index(max(list(d.values())))]





#main
print(more_frecuent(occurence(["Ashot","Shot","Ashot"])))



