# Créé par ASATRYANA, le 05/10/2021 en Python 3.7

import time as t
import datetime as dt
import random as r
import matplotlib.pyplot as plt



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


def get_func_exe_time(func, *arg):

    start_time = dt.datetime.now()
    func(*arg)
    end_time = dt.datetime.now()

    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * (10**3)


    return execution_time




#main-------------------------------------------------------------------
tab_n = 100 #int(inport("Inserer la quantite de tableau : "))
#tabs = [[r.randint(0,1000) for _ in range(0, i+3)] for i in range(tab_n)]

tabs = []

for i in range(tab_n):
    tab = []
    [tab.append(l) for l in [[r.randint(0,1000) for _ in range(i+3)] for _ in range(200)] ] #avec la moyenne

    #sans la moyenne
    #for j in range(0, i+3):
    #    tab.append(r.randint(0,1000))

    tabs.append(tab)

tabs_length = len(tabs)
tab_length = [i for i in range(3,tabs_length + 3) ]


tab_exec_med_time = []
for tab in tabs:
    [tab_exec_med_time.append( round(sum([get_func_exe_time(func, t) for t in tab]) / 200, 5) ) for func in [tri_insertion,tri_selection,sorted]] #avec la moyenne
    #[tab_exec_med_time.append( get_func_exe_time(func, tab) ) for func in [tri_insertion,tri_selection,sorted]] #sans la moyenne




tab_insert_exec_med_time = [tab_exec_med_time[i] for i in range(0, len(tab_exec_med_time), 3)]
tab_select_exec_med_time = [tab_exec_med_time[i] for i in range(1, len(tab_exec_med_time), 3)]
tab_sort_exec_med_time = [tab_exec_med_time[i] for i in range(2, len(tab_exec_med_time), 3)]



fig,axes = plt.subplots()

plt.plot(tab_length, tab_insert_exec_med_time, color="r", label="tri_insertion")
plt.plot(tab_length, tab_select_exec_med_time, color="y", label="tri_selection")
plt.plot(tab_length, tab_sort_exec_med_time, color="cyan", label="sorted")

axes.set(title="Le temps moyen d'execution des algorithms donnés !",
    xlabel="La taille du tableau trié",
    ylabel="Le temps d'éxecution en milisecondes")

plt.legend()
plt.show()
