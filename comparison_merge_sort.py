import random
import os

nbr_comparaison = 0
pourcent = 0
nbr_par_liste = int(input('combien de nombre par liste a trier : '))
v_prct = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def clear_console():       # clear console pour affichage
    os.system('cls' if os.name == 'nt' else 'clear')

def ran():      # generation nombre aleatoire
    global liste
    global non_egual
    n = 0
    while n != nbr_par_liste:
        x = random.randint(0,100)
        n += 1
        if x in non_egual:
            x = random.randint(0,100)
            n -= 1
        else:
            liste.append(x)
            non_egual.append(x)
    print(liste)

def tri_fusion(x):       # tri fusion
    if len(x) == 1:
        return x
    else:
        return fusion(tri_fusion(x[:len(x)//2:]), tri_fusion(x[len(x)//2::]))
def fusion(a,b):
    global nbr_comparaison
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif a[0] <= b[0]:
        nbr_comparaison += 1
        return [a[0]] + fusion(a[1:], b)
    else:
        nbr_comparaison += 1
        return [b[0]] + fusion(a, b[1:])

while 0!=1 :       # boucle principale
    nbr_comparaison = 0
    liste = []
    non_egual = []
    
    n = 0
    while n != nbr_par_liste:
        x = random.randint(0,100)
        n += 1
        if x in non_egual:
            x = random.randint(0,100)
            n -= 1
        else:
            liste.append(x)
            non_egual.append(x)
            
    tri_fusion(liste)
    print(liste)

    for i in range(1,10):
        if nbr_comparaison == i:
            v_prct[i] += 1
            pourcent += 1

    clear_console()
    for i in range(1,10,3):
        print(f'{i}: {int((v_prct[i]/pourcent)*100)}%  {i+1}: {int((v_prct[i+1]/pourcent)*100)}%  {i+2}: {int((v_prct[i+2]/pourcent)*100)}%')
