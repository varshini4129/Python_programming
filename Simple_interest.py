def Simple_Interest(p,n,r):
    SI = p*n*r/100;
    print("the simple interest is",SI)
    return SI
p = int(input("PRINCIPAL : "))
n = int(input("TIME : "))
r = int(input("RATE : "))

Simple_Interest(p,n,r)
