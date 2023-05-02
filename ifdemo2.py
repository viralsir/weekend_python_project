# loop :

rollno=int(input("Enter Roll No:"))
name=input("Enter Name :")
maths=int(input("Enter Maths Marks:"))
if not 0<=maths<=100:   # python ,R
    print("invalid marks")
    maths = int(input("Enter Maths Marks:"))

science=int(input("Enter Science Marks:"))
eng=int(input("Enter English Marks:"))

PASSING_MARKS=35

print("\n output :\n")
print("Roll NO:",rollno)
print("Name:",name)
print("Maths Maks:",maths)
print("Science Marks:",science)
print("English Marks:",eng)


if maths<PASSING_MARKS or science<PASSING_MARKS or eng<PASSING_MARKS:
    print("you are fail")
else:
    print("you are pass")
    total=maths+science+eng
    avg=total/3
    print("Total:",total)
    print("Avg:",avg)
    if avg>90:
        print("Grade : A+")
    elif avg>70:
        print("Grade : A")
    elif avg>55:
        print("Grade : B+")
    else :
        print("Grade : B")






