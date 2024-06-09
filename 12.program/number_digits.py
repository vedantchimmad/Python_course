number=int(input("Enter the number you want to check the digit : "))

counter=0

while number>0:
    number=number//10
    counter+=1


print("Number of the digits are : ",counter)