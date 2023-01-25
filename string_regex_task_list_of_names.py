# you have a list of variable names in camel case format
# ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format
# ["first_item", "friends_list", "my_tuple"]

list_of_names = ["FirstItem", "FriendsList", "MyTuple"]
string_of_names = ", ".join(list_of_names).lower()
string_to_list = string_of_names.split(", ")
print(string_to_list)
