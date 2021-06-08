#Basic code to understand dictionary concept

human_details = [
    {"name" : "Akhil", "age" : 24},
    {"name" : "Aditya", "age" : 23},
    {"name" : "Tanvi", "age" : 22}
]

print(human_details)
print(human_details[0]["name"])

#Loop to access all elements
for elements in human_details:
    print(f"Name of the person is : {elements['name']}")
    print(f"Age of the person is : {elements['age']}")
