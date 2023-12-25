a = ("ADARSH","SHIVAM","SHITAL","DON","RAJA","KING")
print(a)

#lenght of tuple 
print(len(a))

#acess tuple 
print(a[0])
print(a[1])
print(a[-1])
#range function

print(a[1:4])

y=list(a)
y.append("orange")
a= tuple(y)
print(a)