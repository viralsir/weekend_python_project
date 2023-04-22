student_list=[[1,"vimal",23,34,44],[],[]]
rollno=[]
name=[]
maths=[]
sci=[]
eng=[]

for i in range(3):
    rollno.append(int(input("Enter Roll No:")))
    name.append(input("Enter Name:"))
    marks=int(input("Enter Maths Marks:"))
    while not 0<=marks<=100 :
        marks=int(input("Enter Maths Marks:"))
    maths.append(marks)
    marks=int(input("Enter Science Marks:"))
    while not 0<=marks<=100 :
        marks=int(input("Enter Science Marks:"))
    sci.append(marks)
    marks=int(input("Enter English Marks:"))
    while not 0 <= marks <= 100:
        marks = int(input("Enter English Marks:"))
    eng.append(marks)

print("\n output :\n")
for j in range(3):
    print("Roll No:",rollno[j])
    print("Name :",name[j])
    print("Maths Marks:",maths[j])
    print("Science Marks:",sci[j])
    print("English Marks:",eng[j])
    total=maths[j]+sci[j]+eng[j]
    print("total :",total)



