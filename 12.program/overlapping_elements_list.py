L1=[2,4,5,8,1]
L2=[3,4,1,2]
L3=[]
for i in L1:
    if i in L2:
        L3.append(i)

print(L3)