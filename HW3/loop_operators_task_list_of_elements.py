# you have a list of elements [1, 2, 3, 4, 5, 6, 7, 8].
# Loop through the list using the foreach loop.
# The element with an odd index is put into a new list of tuples where
# the first element is the index and the second is the value [(index, value)].
# accordingly, elements with an even index are placed in another
# list of tuples with the same format as in the case with odd indices.

odd_list = []
even_list = []
list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
for index, value in enumerate(list_of_elements):
    if (index % 2) == 0:
        odd_list.append((index, value))
    else:
        even_list.append((index, value))

print(odd_list)
print(even_list)
