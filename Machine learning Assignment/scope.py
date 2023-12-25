#--------------LOCAL VARIABLE--------------------------------------------
def myfunc():
    x = 300
    print(x)
myfunc()

#............................Naming Variables...................................

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
        myinnerfunc 

myfunc()
#--------------------------------------GLOBAL VARIABLE-----------------------------
def myfunc():
  global x
  x = 300

myfunc()

print(x)
