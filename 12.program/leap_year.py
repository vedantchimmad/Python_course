a = int(input("Enter year which you want to check : "))

if a%100==0 and a%400==0:
    print("Year is leap year")

elif a%4==0 and a%100!=0:
    print("Year is leap year")

else:
    print("Year is not a leap year")