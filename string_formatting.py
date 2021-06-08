#String Formatting

#F Strings
name = "Akhil"
name2 = f"Hello {name}"

print(name2)

name = "Jain"
print(name2)

print(f"Hello {name}")

#.format function

firstName = "Akhil"
lastName = "Jain"
statement = "Hello Mr. {} {}"

print(statement.format(firstName, lastName))

firstName = "Vihan"

print(statement.format(firstName, lastName))
