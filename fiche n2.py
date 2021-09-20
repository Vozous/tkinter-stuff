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
        print("Nope ur defenetly vibin")
        play_bat()















#main

#play_bat()










