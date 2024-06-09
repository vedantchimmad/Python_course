number=int(input("Enter the number which you want to check it is palindrome or not :"))

reverse=0
actual_number=number
while number>0:
    digit=number%10
    number=number//10
    reverse=(reverse*10)+digit

if reverse == actual_number:
    print("Entered number is palindrome")
else:
    print("Number is not palindrome")