def Compound_Interest(p,n,r):
    A = p * (pow((1+r/100),n))
    CI = A - p
    print("the simple interest is",CI)
    return CI
p = int(input("PRINCIPAL : "))
n = int(input("TIME : "))
r = float(input("RATE : "))

Compound_Interest(p,n,r)
