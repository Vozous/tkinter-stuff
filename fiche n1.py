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
def in_list (l, n):
    for i in l:
        if n == i:
            return True


def less_n (l, n):
    return len([i for i in l if i < n])


def rev_slice (l, n):
    return l[-n:]



def func_call(func1, func2, func3, l, n):
    return (func1(l, n),
        func2(l, n),
        func3(l, n))



#exercice 6
def concate_sort (l, l1):
    return sorted([*l, *l1])


def rem_dupl_from (l, l1):
    return [i for i in l if i in l1]

def conc_rem_dupl_invsort (l, l1):
    conc_list = [*l, *l1]#fusion les deux list
    list_ = [i for n,i in enumerate(conc_list) if i not in conc_list[:n]]# enlève les doublons
    return sorted(list_, reverse=True)#trie par l'ordre inverse et renvoie la liste finale



#exercice 7
def grades_names ():
    d = {}
    l_noms = ["Armen", "Nil", "Léni", "Flavio"]

    n = 0
    while n < len(l_noms):
        d[l_noms[n]] = [randint(0, 20) for _ in range(5)]

        n += 1

    return d


def get_med_dict (d):
    result = {}

    for k,v in d.items():
        result[k] = sum(v) // len(v)


    return result


def get_best_med (d):
    dk = list(d.keys())
    dv = list(d.values())

    bests = []
    best_med = max(dv)

    for i in dk:
        if d[i] == best_med:
            bests.append(i)


    return " ".join(bests)



def get_best (d):
    dk = list(d.keys())
    dv = list(d.values())
    all_grades = []
    for i in dv:
        for j in i:
            all_grades.append(j)

    bests = []
    bestgrade = max(all_grades)

    for i in dv:
        for j in i:
            if j == bestgrade:

                bests.append(dk[dv.index(i)])
                break

    return " ".join(bests)


def get_med (d):
    dv = list(d.values())

    l = []
    for i in dv:
        for j in i:
            l.append(j)

    return sum(l) // len(l)







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

print("exercice 5" + "\n") #test - exercice 5

list_ = [5,6,1,1,3,5]
print(in_list(list_, 3))#renvoie True si n est présent dans la list_e
print(less_n(list_, 3))
print(rev_slice(list_, 3))
print(func_call(in_list, less_n, slice, l=list_, n=len(list_) // 2))

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------

print("exercice 6" + "\n") #test - exercice 6

list1, list2 = [5,4,7,3,8], [11,33,44,2,4,5,1,6]
print(concate_sort(list1, list2))
print(rem_dupl_from(list1, list2))
print(conc_rem_dupl_invsort(list1, list2))

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------

print("exercice 7" + "\n") #test - exercice 7

my_dict = grades_names()
my_med_dict = get_med_dict(my_dict)

print(my_dict)
print(my_med_dict)
print(get_best_med(my_med_dict))
print(get_best(my_dict))
print(get_med(my_dict))

print("\n" + "-"*20)#alinéa

#-----------------------------------------------------------
