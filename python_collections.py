#Basic exercise on lists, tuples & sets

#lists
l = ["Akhil", "Jain", "Vihan", "Jain", "Vaishali", "Jain", "Madhur", "Jain"]
print(l[0:])
print(l)
print(l[0:3])
print(l[0: :+2])

l.append("Sunita")
l.append("Jain")
print(l)

l.remove("Jain")
print(f"List values are as follows {l}")

#Tuples
#Tuple is immutable
t = ("Akhil","Jain")
print(f"Tuple values are as follows {t}")

#Sets
#Set do not have any order
#Duplicate values are not allowed in set
s = {"Akhil", "Jain", "Vihan", "Jain", "Vaishali", "Jain", "Madhur", "Jain"}
print(f"Set values are as follows {s}")

#Advance Set Operations

#.difference()
friends = {"Aditya", "Govind", "Harshit", "Akhil", "Ankur", "Gaurav"}
abroad = {"Aditya", "Govind", "Harshit"}
local_friends = friends.difference(abroad)

print(f"Friends who live in india are : {local_friends}")

#.union() & .intersection()
PCM = {"Jenish", "Mayank", "Aditya", "Gaurav", "Priyash", "Nikita"}
Commerce = {"Nikita", "Priyash", "Akhil", "Gorish", "Samarth","Vineet"}
Biology = {"Asmita", "Yashi"}

print(f"Friends who studied are : {PCM.union(Commerce.union(Biology))}")
print(f"Friends who studied both PCM and Commerce are : {PCM.intersection(Commerce)}")
