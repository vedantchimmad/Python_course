string1=input("Enter 1st string :")
string2=input("Enter 2nd string :")

if len(string1)!=len(string2):
    print("Strings are not anagram")

else:
    for i in string1:
        if i not in string2:
            print("Entered string is not anagram")
            break

    else:
        print("Entered string is anagram")
