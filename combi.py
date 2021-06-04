"""
# Rappel de la fonction factorielle (n!)

4! = 4*3*2*1 <=> 1*2*3*4
n! = 1*2*3*.*.*n

# Relation du calcul du nombre de combinaisons

(n) = n! / k!*(n-k)!
(k)   
"""

def facto(number):
    # Cas particulier pour 0 factoriel : 0! = 1
    if number == 0:
        return 1
    else:
        F = 1
        for k in range(2, number + 1):
            F = F * k
        return F

def combi(n, k):
    relation = facto(n) / (facto(k) * (facto(n - k)))
    return relation

print(combi(50,3))

# Dezerr