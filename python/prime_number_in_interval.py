def prime(n,m):
    if n <= 1 :  
        print("It is not a prime number")
        return False
    else:
        for i in range(n,m):
            if i%n != 0:
                print(i)

start = int(input("start: "))
stop = int(input("stop: "))
prime(start,stop)
