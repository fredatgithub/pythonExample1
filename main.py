from Utils import IsPrimeByFred
from Utils import IsPrimeByChatGPT

#Exemple utilisation
number = 3321321
result = IsPrimeByFred(number)
if result:
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')

for number in range(1000000,1000990):
    if IsPrimeByChatGPT(number):
        print(f'{number}', end=" ")
print('are prime numbers')