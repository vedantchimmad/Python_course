string=input("Enter string which you wan't to check palindrome :")

reverse=string[::-1]

if string==reverse:
    print("Entered string is palindrome")

else:
    print("Entered string is not palindrome")
    