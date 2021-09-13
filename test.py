from random import randint

#exercice 1
def rect_air (a,b):
	print(f"{a*b:.2f}")



#exercice 2 et 3
def get_rand_list (n=1, manip=False):
    rand_list = [randint(0,100) for _ in range(n+1)]

    if not manip:#sans manipul°
        return rand_list

    else:#avec manipul°
        for i in range(len(rand_list)):
            if not bool(i % 2):#True if i is even
                rand_list[i] *= 10

        return rand_list



#exercice 4
def func (n):
    list = [randint(1,100) for _ in range(n)]
    odd_list = [i for i in list if i%2 == 1]

    print("Multiple de 7 :", [i for i in list if i%7 == 0])#renvoie multiple de 7

    print("Multiple de 9 :", [i for i in list if (i%9 == 0 and i%2 == 0)])#renvoie multiple de 9 et paire

    print("Le produit de max & min des éléments impaires:", max(odd_list) * min(odd_list))



#exercice 5
def func1 ():
    pass



#main-code----------------------------------------------------------------------


print("exercice 1" + "\n")#test - exercice 1

rect_air(2.5,2)

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------

print("exercice 2 et 3" + "\n")#test - exercice 2 et 3

rand_list = get_rand_list(20, manip=True)
print([i for i in rand_list if not bool(i % 2)])#gets even numbers

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------

print("exercice 4" + "\n") #test - exercice 4

func(20)

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------

print("exercice 4" + "\n") #test - exercice 5

func1()

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------




