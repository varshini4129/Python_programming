num = int(input("Enter the number: "))
print("old num : ",num)
rev = 0
num1 = num
while num != 0:
    rem = num%10
    rev = (rev * 10) + rem
    num = num // 10
print("new num : ",rev)
if rev == num1:
    print("it is a palindrome")
else:
    print("its not a palindrome")

print()

word = input("Enter the word: ")
rev = ""
for i in word:
    rev = i + rev
if(word == rev):
    print("it is a palindrome")
else:
    print("its not a palindrome")
