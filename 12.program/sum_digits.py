number=int(input("Enter the number which you want to find the sum of digits : "))


sum=0
while number>0:
    digit=number%10
    sum=sum+digit
    number=number//10

print("Sum of the digit is : ",sum)