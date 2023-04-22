# list=[12,234,4,55,6,77,456,78]

# list1=list[:]
#
# list1.append(123)
# print(list)
# print(list1)

# list1=list[-4:]
# list1.append(123)
# print(list)
# print(list1)
#
# # + operator
# list1=[123,34,55]
# list2=[4,44,55]
# list3=list2 + list1
# print("list1:",list1)
# print("list2:",list2)
# print("list3",list3)
#
# # * operator  for list
# list4=list1*2
# print(list4)
#
# # in operator
# no=int(input("enter no:"))
#
# if no in list1 :
#     print(no," is in list1")
# else:
#     print(no," is not in list1")

#nested list : list of list   each element or some element itself a list.
# list=[12,[33,545],55,66]
# print(list[1][1])
# list.append([1,2,3,4])
# print(list)
# print(list[-1][2])

# person=["vimal","shah","ahmedabad",["9823343216","987654321"]]
# print(person[-1][0])

# list=[[[23,33,55],[12,33],[23,33]],567]
# print(list[0][0][1])
# student=[[[[1,"Vimal",23,23,33]],[],[],[]],[],[],[]]
# student[0][1][2][2]

list1=[12,23,344,544,55]
# iteration -1
# index=0
# while index<len(list1):
#     print(list1[index])
#     index+=1

# iteration - 2
# for count in range(len(list1)):
#     print(list1[count])

#iteration - 3 (forEach loop)
# for element in list1:
#     if element%2==0:
#         print(element)

# diff between append and extends
list1=[1,2,3]
list2=[1,2,3]
list1.append([4,5])
list2.extend([4,5])
print(list1)
print(list2)

name="vimal amit shah"
list=name.split(" ")
print(list)














