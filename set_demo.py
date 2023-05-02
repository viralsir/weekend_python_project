a={1,2,3,4,5,6}
b={4,5,6,7,8}
print(a)

print("intersection using operator :", a&b)
print("intersection using method :",a.intersection(b))

print("difference using operator :", a - b)
print("difference using method :",b.difference(a))

print("union using operator :", a | b)
print("union using method :",a.union(b))

print("symmetric difference  using operator :",a ^ b)
print("symmetric difference using method :",a.symmetric_difference(b))

print("sub set :", a<=b)
print("super set :",a>=b)

print("no of values :",len(a))
print("max :",max(a))
print("min:",min(a))
print("sum",sum(a))

a.remove(3)
a.discard(2)

no=int(input("Enter No:"))
if no  in a :
    print(no," is in the set ")
else :
    print(no," is not in the set")

for element in a :
    print(element)

b.clear()
print("b:",b)
b=set("12345")
b.add(1234)
b.add((12,33))
print("b:",b)

dict={"k":"red","age":42}

for key,value in dict.items():
    print("key :",key,"value:",value)






