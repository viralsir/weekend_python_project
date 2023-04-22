student_list=[]
subject=["Maths","Science","English"]
for i in range(3):
    student=[]
    student.append(int(input("Enter Roll No:")))
    student.append(input("Enter Name:"))
    for index in range(len(subject)):
        marks=int(input("Enter "+subject[index]+" Marks:"))
        while not 0<=marks<=100 :
            marks=int(input("Enter "+subject[index]+" Marks:"))
        student.append(marks)
    student_list.append(student)


print("\n output :\n")
for j in range(len(student_list)):

    print("Roll No:",student_list[j][0])
    print("Name :",student_list[j][1])
    total=0
    for index in range(2,len(student_list[j])):
        print(subject[index-2]," Marks:",student_list[j][index])
        total += student_list[j][index]

    print("total :",total)



