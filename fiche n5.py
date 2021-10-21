
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


def more_frecuent(d,k):
	dkeys,dvals = list(d.keys()), list(d.values())
	klen_mots = [mot for mot in dkeys if len(mot) == k]
	if bool(klen_mots):
		mots_vals = [d[m] for m in klen_mots]

		return klen_mots[mots_vals.index(max(mots_vals))]

	return ""







#main
with open("QuatreVingtTreize.txt") as f:
	text = f.read().split()

print(more_frecuent(occurence(text),7))

