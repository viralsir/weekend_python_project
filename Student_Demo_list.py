student_list=[]
title=["Roll No","Name","Maths","Science","English","Physic"]
for i in range(3):
    student=[]
    student.append(int(input("Enter Roll No:")))
    student.append(input("Enter Name:"))
    subject=title[2:]
    for index in range(len(subject)):
        marks=int(input("Enter "+subject[index]+" Marks:"))
        while not 0<=marks<=100 :
            marks=int(input("Enter "+subject[index]+" Marks:"))
        student.append(marks)
    student_list.append(student)

print("Student list :",student_list)

print("\n output :\n")
for student in student_list:
    for t ,ele in zip(title,student):
        print(t,ele)



