'''
list is unordered data set 
syntax :
to create list use "[]"
'''

a = ['ABC','DEF','XYZ']
print(a)

#Accessing the list 
print(a[1])

#range 
print(a[0:1])

#changing list
a[1]='PQR'
print(a)

#add element in list
a.append('IJK')
print(a)

#remove element in list
a.remove('ABC')
print(a)

#............List Comprehension
newlist=[]
for x in a:
    if "A" in x:
        newlist.append(x)

        print(newlist)

#sorting list
x = [21,43,90,23,1,4,99]
x.sort()
print(x)
