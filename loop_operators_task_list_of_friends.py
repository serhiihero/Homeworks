# You have 2 lists of names friends = ["John", "Marta", "James"]
# and enemies = ["John", "Johnatan", "Artur"].
# Loop through the names of friends and write the message f"{friend} we are the best friends", if the friend is not in the list of enemy names.
# And display the message f"{friend} we are not friends anymore" if the friend is on the list of enemies.
# If the friend's name is James, we don't check him because he is the best friend.

friend_names = ["John", "Marta", "James"]
enemy_names = ["John", "Johnatan", "Artur"]

for friend in friend_names:
    if friend in enemy_names:
        print(f"{friend} we are not friends anymore")
    else:
        if "James" in friend:
            continue
        print(f"{friend} we are the best friends")
