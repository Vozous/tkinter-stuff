from random import randint

#Variables constantes
batinit = 21





#Fonctions predefinies
def play_bat ():
    global batinit

    startinp = input("Welcom Comrade ! Ready to get vibin ? (yes or no)").split(" ")


    if startinp[0] == "yes":

        pleft = False
        while True:
            if batinit <= 0:
                print("Le joueur a perdu") if pleft else print("L'ordi a perdu")

                fininp = input("Voulez vous rejouer ? oui ou non :")
                if  fininp == "oui":
                    batinit = 21
                    continue
                else:
                    break

            print("Il reste {0} bâtonnets en jeu !".format(batinit))

            #player
            batretirep = int(input("Combien retirez-vous de bâtonnets : "))

            batinit -= batretirep
            pleft = True
            print(f"Le joueur a retiré {batretirep} bâtonnets !")

            if batinit <= 0: continue

            print("Il reste {0} bâtonnets en jeu !".format(batinit))

            #ordi
            batretireord = 1 if batinit <= 2 else randint(1,3)
            pleft = False
            batinit = batinit - batretireord
            print(f"L'ordinateur a retiré {batretireord}")

            if batinit <= 0: continue






    else:
        print("Nope ur defenetly vibe-in")
        play_bat()



def vect_dist(vect1, vect2):

    return ((vect1[0]-vect2[0])**2 + (vect1[1]-vect2[1])** 2 + (vect1[2]-vect2[2])**2)



def submarine_pos_dist (nom="Alpha, Delta", pos=[[0,0,0], [0,0,0]]):
    nompos = list(zip(nom.split(", "), pos))
    currentpos = [0,0,0]
    visited = [] 
    dist = 0

    while len(visited) < len(nom.split(", ")):
        distfromcurrent = [vect_dist(currentpos, i[1]) for i in nompos if not (i[0] in visited)]

 

        for i in nompos:
            n,p = i[0], i[1]#le nom et le position

            if not (n in visited):
                if vect_dist(currentpos,p) == min(distfromcurrent):
                    print(n)
                    visited.append(n)
                    dist += vect_dist(currentpos,p)
                    currentpos = p

                    break






        print("---------",len(visited), len(nom.split(", ")))
        

    return f"La distence totale est de {dist} !"



def epidemic_data_treat (data1=[[]], data2=[[]]):
    dtnoms = sorted(set([i[0] for i in data1]))
    bilan = list(zip([i[0] for i in data1], [i[2] for i in data1], [i[2] for i in data2], [i[3] for i in data1], [i[4] for i in data1]))

    print(dtnoms)
    print(bilan)

    











#main

#play_bat()

pos = [[134,67,123], [128,-92,-50], [-45,137,5], [-196,140,-174], [10,2,302], [234,-313,-255]]
nom = "Alpha, Beta, Gamma, Delta, Epsilion, Zeta"
#print(submarine_pos_dist(nom=nom, pos=pos))

fievre_jaune = [['Bénin','BJ',2010,14530,376],['Mail','ML',2009,32645,946], ['Mali','ML',2010,29365,487], ['Liberia','LR',2009,13833,644], ['Liberia','LR',2010,8348,234], ['Liberia','LR',2011,1405,98], ['Perou','PE',2011,56934,1354]]
population = [['Bjn',2010,9199254], ['Ml',2009,14581427], ['ML',2010,15049352], ['LR',2009,3754129], ['LR',2010,3891357], ['LR',2011,4017446], ['PE',2010,29027680], ['PE',2011,29264314]] 
epidemic_data_treat(data1=fievre_jaune, data2=population)
