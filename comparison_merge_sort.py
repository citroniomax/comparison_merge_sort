import random
import os

def console():      # clear console pour affichage
    os.system('cls' if os.name == 'nt' else 'clear')

console()
nbr_comp = 0
pourcent = 0
nbr_par_liste = int(input('combien de nombre par liste a trier (1 - 100) : '))
v_prct = []

for _ in range(603):       # creation des compteurs par nombre de comparaisons (ici 1000)
    v_prct.append(0)

def aff(x):     # fonction d'affichage
    return int((v_prct[x]/pourcent)*100)

def tri_fusion(x):       # tri fusion
    if len(x) == 1:
        return x
    else:
        return fusion(tri_fusion(x[:len(x)//2:]), tri_fusion(x[len(x)//2::]))
def fusion(a,b):
    global nbr_comp
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif a[0] <= b[0]:
        nbr_comp += 1
        return [a[0]] + fusion(a[1:], b)
    else:
        nbr_comp += 1
        return [b[0]] + fusion(a, b[1:])

while 0!=1 :       # boucle principale
    nbr_comp = 0
    liste = []
    non_egual = []
    
    n = 0   
    while n != nbr_par_liste:       # genere liste random
        x = random.randint(0,100)
        n += 1
        if x in non_egual:      # il faut avoir x nombres DIFFERENTS dans la liste (enoncé eval)
            x = random.randint(0,100)
            n -= 1
        else:
            liste.append(x)
            non_egual.append(x)
            
    tri_fusion(liste)

    for i in range(1,603):         # inscrit nbr_comp dans le bon index v_prct
        if nbr_comp == i: 
            v_prct[i] += 1
            pourcent += 1
            
    console()
    
    for i in range(1,600,3):
        if v_prct[i] + v_prct[i+1] + v_prct[i+2] != 0:      # si que des 0%, inutile d'afficher
            if aff(i) + aff(i+1) + aff(i+2) != 0:
                print(f'{i}: {aff(i)}%  {i+1}: {aff(i+1)}%  {i+2}: {aff(i+2)}%')
    
    print('')
    print(liste)        # affiche chaque liste utilisé
