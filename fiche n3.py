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
    execution_time = time_diff.total_seconds() * 10000


    return execution_time




#main-------------------------------------------------------------------
tab_n = 98 #int(inport("Inserer la quantite de tableau : "))
#tabs = [[r.randint(0,1000) for _ in range(0, i+3)] for i in range(tab_n)]

tabs = []

for i in range(tab_n):
    tab = []
    for j in range(0, i+3):
        tab.append([r.randint(0,1000) for _ in range(100)])

    tabs.append(tab)



tab_exec_med_time = []
for tab in tabs:
    [tab_exec_med_time.append( round(sum([get_func_exe_time(func, t) for t in tab]) / 100, 5) ) for func in [tri_insertion,tri_selection,sorted]]


tab_insert_exec_med_time = [tab_exec_med_time[i] for i in range(0, len(tab_exec_med_time) // 3, 3)]
tab_select_exec_med_time = [tab_exec_med_time[i] for i in range(1, len(tab_exec_med_time) // 3, 3)]
tab_sort_exec_med_time = [tab_exec_med_time[i] for i in range(2, len(tab_exec_med_time) // 3, 3)]

fig,axes = plt.subplots()

plt.plot(tab_insert_exec_med_time)
plt.plot(tab_select_exec_med_time)
plt.plot(tab_sort_exec_med_time)

plt.show()