#List Comprehension in python

friends = ["Tanvi", "Taniya", "Tanuj", "Tinku", "Tarun", "Akhil", "Sanyam"]
friends_s = [friend for friend in friends if friend.startswith("T")]

print(friends_s)

friend_list = []
#Alternativeloop for same
for friend in friends:
    if friend.startswith("T") == True:
        friend_list.append(friend)

print(friend_list)

print(friend_list is friends_s)
