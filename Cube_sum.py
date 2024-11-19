num = int(input("enter the number : "))
sum = 0
for i in range(1,num+1):
    sq = i*i*i
    sum += sq
print("The Sum of squares of first n natural numbers is ",sum)
