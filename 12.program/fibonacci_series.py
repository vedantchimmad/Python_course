terms=int(input("Enter number of terms you want to get fibonacci series :"))

a=0
b=1

for i in range(terms):
    c=a+b
    a=b
    b=c
    print(c)