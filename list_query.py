list1=[1,2,3]
list2=[4,5,6]


list2.append(list1[:])
list1.append(23)
print("list1:",list1)
print("list2:",list2)
