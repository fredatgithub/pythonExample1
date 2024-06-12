import sys

from Utils import IsPrimeByFred
from Utils import IsPrimeByChatGPT

#Exemple utilisation
number = 3321321
result = IsPrimeByFred(number)
if result:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')

#for number in range(1000000,1000990):
#intMaxSize = 9223372036854775807
intMaxSize = 500000000
compteur = 0
lastdifference = 0
lastPrime = 2
liste_de_difference = []
line = ''
for number in range(2, intMaxSize):
    if IsPrimeByChatGPT(number):
        #print(f'{number}', end=" ")
        lastdifference = number - lastPrime
        lastPrime = number
        print(f'{number} différence = {lastdifference}')
        line = f'{number} - {lastdifference}'
        liste_de_difference.append(line)
        compteur += 1
print('are prime numbers')

#La taille maximale d'un entier sur cette plateforme est : 9_223_372_036_854_775_807 ou 9223372036854775807
print("La taille maximale d'un entier sur cette plateforme est :", sys.maxsize)

# Ouvrir un fichier en mode écriture
with open('PrimeDifference2-500Millions.txt', 'w') as fichier:
    fichier.write("Différence des nombres premiers de 2 à 100_000_000\n")
    for element in liste_de_difference:
        fichier.write(str(element) + "\n")

print('Fichier écrit')
