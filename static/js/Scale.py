sum = 0
scale = int(input("Enter your scale: "))

for i in range(4):
    num = int(input("Enter a number: "))
    sum = sum + num

if sum > scale:
    print("Summation is more than scale!")