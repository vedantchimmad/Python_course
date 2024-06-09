number = int(input("Enter the number to get the factors :"))

for i in range(1,number+1):
    if number%i==0:
        print(i)


