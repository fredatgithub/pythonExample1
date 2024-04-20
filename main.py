number = 3321321

# To take input from the user
# number = int(input("Enter a number: "))

if number == 1:
    print(number, 'is not a prime number')
elif number > 1:
    # check for factors
    for i in range(2, number):
        if (number % i) == 0:
            print(number, 'is not a prime number')
            print(i, 'times', number // i, 'is', number)
            break
    else:
        print(number, 'is a prime number')

# if input number is less than
# or equal to 1, it is not prime
else:
    print(number, 'is not a prime number')


    def check_prime(number):
        if number == 1:
            return f"{number} is not a prime number"
        elif number > 1:
            # check for factors
            for i in range(2, number):
                if (number % i) == 0:
                    return f"{number} is not a prime number\n{i} times {number // i} is {number}"
                    break
            else:
                return f"{number} is a prime number"
        else:
            return f"{number} is not a prime number"


    # Exemple d'utilisation
    number = 3321321
    result = check_prime(number)
    print(result)