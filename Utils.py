def check_prime(number):
        if number == 1:
            return f"{number} is not a prime number"
        elif number > 1:
            # check for factors
            for i in range(2, number):
                if (number % i) == 0:
                    return f"{number} is not a prime number\n{i} times {number // i} is {number}"
            else:
                return f"{number} is a prime number"
        else:
            return f"{number} is not a prime number"

def IsPrime(number):
        if number == 1:
            return False
        elif number > 1:
            # check for factors
            for i in range(2, number):
                if (number % i) == 0:
                    return False
            else:
                return True
        else:
            return False

def IsPrimeByFred(number):
     if number == 1 or number == 0:
        return False
     if number == 2 or number == 3 or number == 5:
        return True
     if number % 2 == 0 or number % 3 == 0 or number % 5 == 0:
        return False
     for divisor in range(7, number ** 2, 2):
        if number % divisor == 0:
            return False
     return True
