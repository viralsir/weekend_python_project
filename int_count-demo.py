# PALINDROME NO  =>  121  ,1221    1 TO 1000
# no=input("Enter No:")
# print(no)
# print("no of digit :",len(no))
# no_of_digit=len(no)
# no=int(no)
#  22 * 33
#no=int(input("Enter No:"))
for no in range(100,1000):
    original_no=no;
    sum=0;
    count=0
    while no>0:
        sum = sum + ((no % 10)**3)
        no=no//10;
        count=count+1

    if sum==original_no:
        print(original_no)
    # else :
    #     print(original_no," is not a armstrong no")

# print("count:",count)
# print("Sum:",sum)
# print("original no:",original_no)