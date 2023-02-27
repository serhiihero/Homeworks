# you have a list of variable names in camel case format
# ["FirstItem", "FriendsList", "MyTuple"]
# convert it to a list of variable names for python in snake case format
# ["first_item", "friends_list", "my_tuple"]
import re

list_of_names = ["FirstItem", "FriendsList", "MyTuple"]
pattern = re.compile(r'([A-Z][a-z]+)([A-Z][a-z]+)')
divide_set_of_names = pattern.sub(r'\1_\2', ','.join(list_of_names)).lower()

result = divide_set_of_names.split(',')
print(divide_set_of_names)