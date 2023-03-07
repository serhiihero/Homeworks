# You have the number 2 as a variable.
# Multiply it by 2 in two ways.
# Accordingly, you need to divide it in 2 different ways by 2.

number = 2
number_in_bin = int(bin(0b10), 2)
print(number * 2)
print(number * number_in_bin)
print(number / 2)
print(number / number_in_bin)
