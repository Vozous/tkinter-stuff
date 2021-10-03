import time as t
import random as r
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')

#functions
def tri_insertion(tab): 
    for i in range(1, len(tab)): 
        k = tab[i] 
        j = i-1
        while j >= 0 and k < tab[j] : 
                tab[j + 1] = tab[j] 
                j -= 1
        tab[j + 1] = k

    return tab



def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp

   return tab


def get_func_exe_time(func, arg):
    start_time = t.time()
    func(arg)
    return float(t.time() - start_time) * 1000




#main-------------------------------------------------------------------
tab_n = 500 #int(inport("Inserer la quantite de tableau : "))
tabs = [[r.randint(0,1000) for _ in range(0,i+3)] for i in range(tab_n)]

fig,ax = plt.subplots()


for i in :

    plt.scatter(x, y, marker='o', label)




#tri par insertion
x,y = [len(i) for i in tabs], [get_func_exe_time(tri_insertion, i) for i in tabs]
plt.plot(x, y, color="r", label="tri_insertion()")
print(y)
#tri par selection
x,y = [len(i) for i in tabs], [get_func_exe_time(tri_selection, i) for i in tabs]
plt.plot(x, y, color="g", label="tri_selection()")
print(y)
#tri par sorted
x,y = [len(i) for i in tabs], [get_func_exe_time(sorted, i) for i in tabs]
print(y)
plt.plot(x, y, color="b", label="sorted()")

ax.set(xlim=(0, tab_n), ylim=(0, 2),
       xlabel='tab length', ylabel='execution time',
       )

plt.show()