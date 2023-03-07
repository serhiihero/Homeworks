# You have a group of people with non-unique names.
# Generate a list of non-duplicate names (you cannot use set for this task.
# If there are 2 johns in the list, you need to take only one of them. "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

users_list = ["Selena", "Nils", "Arman", "Jossy", "Belek", "Jack", "Nils", "Barak", "Kenny", "Belek"]
users_list = list(dict.fromkeys(users_list))
print(users_list)
