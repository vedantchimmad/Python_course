number = int(input("Enter to the number to check whether it is  prime or not :"))

count=0
for i in range(1,number+1):
    if number%i==0:
        count+=1

if count>2:
    print("Number is not a prime number ")

else:
    print("Number is a prime number ")