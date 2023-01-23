Sports= {'indoor':'Ludo,cards and video games', 
        'OutDoor' :'Kho-Kho, cricket, volleyball, basketball and football'}
print("ALL Elements:\n",Sports)

#clear
Sports.popitem()
print(Sports)

#Copy
Sports = Sports.copy()
print(Sports)

#values
x = Sports.values()
print(x)

#update
Sports.update({"indoor": "Chess" ,"OutDoor": "kabaddi"})

print(Sports)

#Get
x = Sports.get("Get:","OutDoor")

print(x)



