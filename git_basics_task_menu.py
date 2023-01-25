# You have two groups of people.
# One group consists of omnivores, the other only vegetarians.
# An omnivore is a vegetarian but a vegetarian is not an omnivore.
# Display a list of guests who can eat vegetables and herbs.

omnivores = ["Greg", "Postel", "Bastion", "Derek"]
vegetarian = ["Amanda", "Coursel", "Derek"]
omnivores.extend(vegetarian)
print(omnivores)
