#Taking Input from user

name = input("What is your name : ")
print(name)

#Calculating Square

number = input("Please enter number for calculating square : ")
converting_to_no = int(number)
calc_number = converting_to_no * converting_to_no
print(calc_number)

#Calculating Square metres

size = input("Tell me how big is your house in (square metres) : ")
square_feet = int(size)
square_metres = square_feet / 10.8
print(f"Size in square metres is {square_metres:.2f}")