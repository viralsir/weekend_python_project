# dict1={'first':1,2:"second"}
#
# print(dict1)
# print(dict1['first'])
# dict1['first']=122
# print(dict1)
# dict1['city']='ahmedabad'
# print(dict1)
# dict1['list']=[12,33,44]
# print(dict1)
# print(dict1['list'])


#person=["vimal","naranpura",34343434,]
# person={"name":"vimal","address":"naranpura",
#         "phno":{"home":232332,"office":2323334}}
# print(person)
# print(person["name"])
# print(person["phno"]["home"])


dict={}
#dict.__setitem__(input("Enter Key:"),int(input("Enter Value:")))
#dict.__setitem__("Rollno",int(input("Enter Roll No:")))
# dict["rollno"]=int(input("Enter Roll No:"))
# dict["name"]=input("Enter Name");
# print(dict)
# print("length:",len(dict))
# print("keys",dict.keys())
# print("vaues:",dict.values())
# print("items:",dict.items())

# print("\n Keys:")
# for key in dict.keys():
#     print(key)
# print("\n Values :")
# for value in dict.values():
#     print(value)
# print("\n items :")
# for key,value in dict.items():
#     print(key,":",value)


# list within dict
dict={"rollno":1,"name":"vimal","marks":[12,23,44]}
print(dict["marks"])
dict["marks"].append(55)
print(dict["marks"])

# dict within list
studentlist=[{"rollno":1,"name":"vimal","maths":23,"science":34},
             {"rollno":2,"name":"viren","maths":55,"science":45},
             {"rollno":1,"name":"vimal","maths":73,"science":84},
             {"rollno":2,"name":"viren","maths":55,"science":95},
             {"rollno":1,"name":"vimal","maths":20,"science":34},
             {"rollno":2,"name":"viren","maths":85,"science":45}
            ]

#print(studentlist[1]["maths"])
for student in studentlist:
   #print(student["maths"])
   for key,value in student.items():
        print(key,":",value)

maths_list=[student["maths"] for student in studentlist]
total_marks_list=[student["maths"]+student["science"] for student in studentlist]
avg_list=[total/2 for total in total_marks_list]
print(maths_list)
print(total_marks_list)
print(avg_list)
avg_list.sort(reverse=True)
print("top three :",avg_list[1])


































