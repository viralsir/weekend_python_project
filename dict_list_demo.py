'''
     Std_Student=[{A:[{"rollno":1,"name":},{},{}],B:[],c:[]},{},{},{}]
     view : pass and fail  ,grade
     search : by roll no
'''

Std_Student=[]
title =["Roll No:","Name:","Maths:","Science:","English:"]
for ele in range(1,13):
    dict={}
    for i in "ABCD":
        dict[i]=[]
    Std_Student.append(dict)
print("Std_Student List",Std_Student)
option=1
while option!=13 :
    print("\n\n\t\t\t LML School ")
    option=int(input("Enter Standard (1to12) (13 for Exit):"))
    if not 1<=option<=13:
        print("\n wrong option selected")
    elif option==13:
        print("you are exited")
    else :
        option2=0
        while option2 != 3:
                print("\n\t\t Std - ",option)
                print("\n\t\t press 0 for Entry ")
                print("\n\t\t press 1 for View ")
                print("\n\t\t press 3 for Main Menu")

                option2=int(input("Enter option:"))

                if option2==0:
                    div=input("Enter Division(A to D):")
                    #div=div.upper()

                    while div not in "ABCD" :
                        div = input("Enter Division(A to D):")
                        div = div.upper()
                    option3="Y"
                    while option3=="Y":
                        student={}
                        student[title[0]]=input("Enter "+title[0])
                        student[title[1]]=input("Enter "+title[1])
                        for t in title[2:]:
                            student[t]=int(input("Enter "+t))
                        Std_Student[option-1][div].append(student)
                        option3=input("do you want to Continue(Y/N)?:")
                        option3=option3.upper()
                elif option2==1:
                    print("Std_std:",Std_Student)
                    div = input("Enter Division(A to D):")
                    div = div.upper()
                    while div not in "ABCD":
                        div = input("Enter Division(A to D):")
                        div = div.upper()
                    for student in Std_Student[option-1][div]:
                        print("student :",student)
                        for key,value in student.items():
                            print(key,value)
                elif option2==3:
                    print("Back to main menu")
                else :
                    print("wrong option selected try again !")
