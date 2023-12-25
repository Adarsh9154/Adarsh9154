Marks = {"ADARSH": 98 , "KARAN":78 , "ARPIT": 39, "PIYUSH": 71}
print(Marks)

#student marks 
print(Marks["ADARSH"])
print(Marks["KARAN"])
print(Marks["ARPIT"])

#Length of dictionaries
print(len(Marks))

x = Marks["PIYUSH"]
print(x)

#changing Marks 
Marks.update({"PIYUSH" : 83})
print(Marks)

#add marks 
Marks["ANKUSH"]= 91
print(Marks)

#delete marks
Marks.pop("KARAN")
print(Marks)

#clear marks
Marks.clear()
print(Marks)

#Nested marks 
details = {
    'STUDENT1':{
        "name" :'Adarsh','year': 2004
    },
    'STUDENT2':{
        'name':'Karan','year': 2003
    },
    'STUDENT3':{
        'name':'Arsh','year': 2002
    }
}
print(details)

#accessing 
print(details['STUDENT1']['name'])