num = int(input("Enter the number : "))
c = 0
while num > 0:
    rem = num%1
    c += 1
    num = num // 10
print(f"the count of the digit is : {c}")
    
