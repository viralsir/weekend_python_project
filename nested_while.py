no=int(input("Enter No:"))
i=1
m=1
while i<=2*no-1:
    j=no+1
    while j>=1:
        if j>m :
            print(" ",end="")
        else:
            print(j,end=" ")
        j=j-1
    print("")
    if i<no:
        m=m+1
    else :
        m=m-1
    i=i+1


'''


output :
1
12
123
1234
12345

'''