number=int(input("Enter to find the factorial of a number :"))

factorial=1
for i in range(number,1,-1):
    factorial=number * factorial
    number-=1

print("Factorial of the given number is :",factorial)
