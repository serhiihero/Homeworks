# Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
#   a. element is an integer that will be the left operand of the expression
#   b. element is an integer that will be the right operand of the expression
#   c. element is an integer from 1 to 3 where:
#       identifies the addition operation
#       identifies the subtraction operation
#       identifies the multiplication operation
# d. You can put data into a text file with the text form or use the pickle module in binary form.
# If placed as text then each line should contain only elements of one tuple separated by spaces (eg "100 2 3").
# The file must be created by a script in a pre-created \test\data directory tree.
# The directory tree must be created by the script.
# Push only the code to the repository (not directories or file).
import os
import random
import operator

if __name__ == '__main__':
    list_of_tuples = []
    data = 0
    math_operators = {
        1: operator.add,
        2: operator.sub,
        3: operator.mul
    }
    while data < 100:
        left_operand = random.randint(1, 50)
        right_operand = random.randint(1, 50)
        math_key = random.choice(list(math_operators.keys()))
        list_of_tuples.append(
            (left_operand, right_operand, math_key))
        data += 1

    print(list_of_tuples)
    os.makedirs("./test/data")
    with open('./test/data/text_file.txt', 'w') as file:
        file.write('\n'.join('{} {} {}'.format(key[0], key[1], key[2]) for key in list_of_tuples))
        file.close()