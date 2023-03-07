# Using the created file in task 1, read the file and perform mathematical operations on each element.
# Output the result of the operation to the console. You cannot use imports to import from the first task module.
import operator

if __name__ == '__main__':
    with open('./test/data/text_file.txt', 'r') as file:
        file_content = file.readlines()
        file_content = list(map(lambda x: x.replace('\n', ''), file_content))
        math_operators = {
            1: operator.add,
            2: operator.sub,
            3: operator.mul
        }
        print(file_content)
        for data in file_content:
            divide_string = data.split(' ')
            numbers = list(map(int, divide_string))
            math = math_operators[numbers[2]](numbers[0], numbers[1])
            print(math)
