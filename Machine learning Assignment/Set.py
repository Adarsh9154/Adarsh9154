#here we use {}
#to create set 
a = {"ADARSH","ROHAN","KARAN"}
print(a)

#duplicate set element not allowed
b = {"ADARSH","ROHAN","KARAN","ADARSH"}
print(b)

#length of set
print(len(b))

#access 
for x in b:
    print(x)

#check element in set
print("ROHAN" in b)

#add element of set 
b.add("KIRAN")
print(b)

#two set in one set
c= {"ARUN","VIRU"}
b.update(c)
print(b)

#remove element from set
b.remove("ADARSH")
print(b)
#or we can use pop method 
x= b.pop()
print(x)
print(b)

