var = [1,2,3,4,5,6,7,8,9]
head, *tail = var

print(head)
print(tail)

*head, tail = var

print(head)
print(tail)