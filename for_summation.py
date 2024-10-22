#for Summation code here
num = int(input("Enter a positive number: "))
loops = 0
sum = 0
for loops in range(num):
    loops = loops +1
    sum = sum + loops
print("The summation of " + str(num) + " is " + str(sum))
