from math import sqrt, floor


def is_prime(n):

    if n < 2:
        return False

    #1st number in range() function is inclusive, 2nd is exclusive
    for i in range (2, floor(sqrt(n)) +1 ):
        if n % i == 0:
            return False
        
    return True

print(f"\n{is_prime(83)}")