# homework division wise entry and view and update
student_list=[]
title=["Roll No","Name","Maths","Science","English","Physic"]

option=1
while option!=3 :
    print("\n\t\t\t Student corner \n")
    print("\t\t press 1 for Entry ")
    print("\t\t press 2 for View ")
    print("\t\t press 3 for Exit")

    option=int(input("Enter option:"))

    if option==1:
        option2=0
        while option2==0:
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
            option2=int(input("press 0 for Continue:"))

    elif option==2:
        for student in student_list:
            for t ,ele in zip(title,student):
                print(t,ele)

    elif option==3:
        print("You are exited");
    else :
        print("Wrong option selected try again !")


