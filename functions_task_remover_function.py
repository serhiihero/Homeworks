# 4. You have a file of unknown length.
# Write a function that will remove all numbers from each line of the file.
import re


def number_remover(processed_content: str) -> str:
    return re.sub(r'\d', '', processed_content)


if __name__ == '__main__':
    with open('data.txt', 'r') as file:
        data_file = file.read()
    print(number_remover(data_file))
