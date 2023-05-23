import random
import os

nbr_comparaison = 0
print_ = 0
v4 = 0
v5 = 0
v6 = 0
v7 = 0
v8 = 0
v9 = 0

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def ran():
    global liste
    global non_egual
    n = 0
    while n != 5:
        x = random.randint(0,100)
        n += 1
        if x in non_egual:
            x = random.randint(0,100)
            n -= 1
        else:
            liste.append(x)
            non_egual.append(x)
    print(liste)

def triFusion(x):
    if len(x) == 1:
        return x
    else:
        return fusion(triFusion(x[:len(x)//2:]), triFusion(x[len(x)//2::]))
    
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

while 0!=1 :
    nbr_comparaison = 0
    print_ += 1
    liste = []
    non_egual = []
    ran()
    triFusion(liste)
    if nbr_comparaison == 4:
        v4 += 1
    elif nbr_comparaison == 5:
        v5 += 1
    elif nbr_comparaison == 6:
        v6 += 1
    elif nbr_comparaison == 7:
        v7 += 1
    elif nbr_comparaison == 8:
        v8 += 1
    elif nbr_comparaison == 9:
        v9 += 1
    pourcent = v4 + v5 + v6 + v7 + v8 + v9
    clear_console()
    print(f'4: {int((v4/pourcent)*100)}%  5: {int((v5/pourcent)*100)}%  6: {int((v6/pourcent)*100)}%  7: {int((v7/pourcent)*100)}%  8: {int((v8/pourcent)*100)}%  9: {int((v9/pourcent)*100)}%')
    


'''print(liste)
print(triFusion(liste))
print(f'Il y a eu {nbr_comparaison} comparaisons.')'''

