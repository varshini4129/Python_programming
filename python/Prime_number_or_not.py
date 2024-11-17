from math import sqrt

def prime(n):
    if n <= 1:  
        print("It is not a prime number")
        return False
    else:
        sqt = int(sqrt(n))  
        for i in range(2, sqt + 1):
            if n % i == 0:  
                print("It is not a prime number")
                return False
        print("It is a prime number") 
        return True

n = int(input("Enter the number: "))
prime(n)
