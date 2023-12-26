#python IF else statement 
i = 7
if (i>24):
    print("IM HERO")
    print("ABC")

else:
    print("IM VILLAN")
    print("XYZ")

print("python if else statement")

#nested if statement 
if(i==7):
    if(i < 15):
        print("i is smaller than 15")

    if(i < 12):
        print("i is less 12 too")
    else:
            print("i is greater than 12")

# if-elif-else 
x = 20 
if(x == 10):
    print("x is 10")
elif(x == 15):
    print("x is 15")  
elif(x == 20):
    print("x is 20")
else:
        print("x is not here")


#For loop 
a = ["ABC","DEF","FGH"]

for i in a:
    print(i)



for i in range(0,20,2):
    print(i)

#Loop inside a For Loop
for i in range(0,4):
    for j in range(0,4):
        print(i,j)

# zip() function is used to add two list in parallel
HOBIES = ["FOOTBALL","GAMING","CODING"]
VIBES = ["LOVE", "ADDICTION","INTREST"]
for HOBIES , VIBES in zip(HOBIES, VIBES):
    print(HOBIES , "IS", VIBES)

#Continue statements 
for letter in 'adarshmundhe':
    if letter == 'd' or letter == 'e':
        continue
    print('Current letter:',letter)

#break statement
for letter in 'adarshmundhe':
    if letter == 'd' or letter == 'e':
        break
    print('Current letter:',letter)

#pass statement
for letter in 'adarshmundhe':
    pass
print('last letter:',letter)

#loop in range function 
for i in range(10):
    print(i,end="  ")
sum=0 
for i in range(1,10):
    sum = sum+i 
    print("the sum is :",sum)