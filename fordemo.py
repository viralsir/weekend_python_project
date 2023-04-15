'''
    for
        syntax : for  element in range(start,end,step):
                        statement

     0



start=int(input("enter Stating no:"))
end=int(input("Enter Ending no:"))
for i in range(start,end,5):
    print(i)


for i in range(50,5,-5):
    print(i)


for i in range(1,6):
    for j in range(6,0,-1):
        if j>i :
            print(end=" ")
        else:
            print(j,end=" ")
    print("")

#no=int(input("Enter No:"))

for no in range(1,101):
    is_prime=True;
    for i in range(2,no):
        if no%i == 0 :
            is_prime=False
            break

    if is_prime :
        print(no,end=",")
'''
# armstrong number   153  ==  1 +125 +27 => 153
#153  1.53
no=int(input("Enter No:"))


# find armstrong no between 100 to 999
# print("division : ", no/100)
# print("Integer division :", no//100)
# print("module :", no%100)
#print(no**3)


first_digit=no//100;
second_digit=(no//10)%10
third_digit=no%10

#sum=(first_digit*first_digit*first_digit)+(second_digit*second_digit*second_digit)+(third_digit*third_digit*third_digit)
sum=first_digit**3 + second_digit**3 + third_digit**3
if no==sum :
    print(no," is a armstrong no")
else:
    print(no," is not a armstrong no")


























