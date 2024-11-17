def fibo(n):
    if(n <= 0):
        print("invalid input")
    elif(n == 1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
n = int(input("enter the number: "))
print(fibo(n))
