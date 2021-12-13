#fonctions
def find_min(l):	
	longueur = len(l) 
	assert isinstance(l, list), "Error, first parameter requires a list !" #revoie une eurreur si l n'est pas une instance de list
	assert longueur != 0, "Error, list shoudn't be empty !" #revoie une erreur si l est vide

	mini = l[0]
	i = 1
	while i < longueur: #tant que i (counter) est plus petit longueur
		if l[i] < mini: #i em element est plus petit que le minim choisi<<<<<<<<<<<<<<
			mini = l[i]
		i += 1
	
	return mini


def open_file(fname):
	assert  isinstance(fname, str), "Error file name shoudn be a string !" #renvoie une erreur si fname n'est pas un string
	assert len(fname) != 0, "Error, file name shoudn't be empty !" #revoie une erreur si fname est vide

	try:
		with open(fname, "r") as file:
			return tuple(file.read())

	except FileNotFoundError:
		print("-------Erreure : Fichier introuvable !")


def passworld_validate():
	password = str(input("Enter your password : "))
	valid_result = ""

	#At least 8 symboles
	valid_result += "-'At least 8 elements needed'-" if len(password) < 8 else ""

	#Minimum 3 digits:
	valid_result += "'Minimum 3 digitsneeded'-" if len([n for n in password if n.isdigit()]) < 3 else "" 

	#At least one uppercase
	valid_result += "'Minimum one uppercase character'-" if len([char for char in password if char.isuppercase()]) < 1 else "" 

	#At least two of special characters : #, @, |, ~, $ 
	valid_result += "'At least two of special characters : #, @, |, ~, $'-" if  else "" 




#main
