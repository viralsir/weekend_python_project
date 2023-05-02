'''

     Relational Operator

     operator               symbol
     grater than            >
     less than              <
     equal to               ==
     not equal to           !=
     grater than or
     equal to               >=
     less than or
     equal to               <=


       Logical Operator
       operator             symbol
       and                   and       both true part
       or                     or        any of the true part;
       not                   not       true ->false



    if   condition :
        true part;
        statement ;
    else :
        false part;
        statement;

'''
# no1=int(input("Enter no1:"))
# no2=int(input("Enter No2:"))
#
# if no1>no2:
#     print(no1," is a maximum no")
# else :
#     print(no2," is a maximum no")
#
# print("outside if ")



# no1=int(input("Enter no1:"))
# no2=int(input("Enter No2:"))
# no3=int(input("Enter No3:"))
#
# if no1>no2 and no1>no3:
#     print(no1," is a maximum no")
# elif no2>no3 and no2>no1 :
#     print(no2," is a maximum no")
# elif no3>no1 and no3>no2:
#     print(no3," is a maximum no")
# else :
#     print("out of three two value might be same")
#
# print("outside if ")


# no1=int(input("Enter no1:"))
# no2=int(input("Enter No2:"))
# no3=int(input("Enter No3:"))
#
# if no1>=no2 and no1>=no3:
#     print(no1," is a maximum no")
# elif no2>=no3 and no2>=no1 :
#     print(no2," is a maximum no")
# else :
#     print(no3," is a maximum no")
#
# print("outside if ")


no1=int(input("Enter no1:"))
no2=int(input("Enter No2:"))
no3=int(input("Enter No3:"))

if no1>0 and no2>0 and no3>0 :
    # nested if
    if no1>no2 and no1>no3:
        print(no1," is a maximum no")
    elif no2>no3 and no2>no1 :
        print(no2," is a maximum no")
    elif no3>no1 and no3>no2:
        print(no3," is a maximum no")
    else :
        print("out of three two value might be same")

else :
    print("invalid input ")

print("outside if ")










