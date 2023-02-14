# You have the file text.txt(attached). Please count how many times each letter appears in this file.

if __name__ == '__main__':
    with open('./test/data/text_file.txt', 'r') as file:
        file_content = file.read().replace('\n', ' ')
        content_splited = file_content.split(' ')
    characters = {}
    for character in file_content:
        if character in characters:
            characters[character] += 1
        elif character == ' ':
            pass
        else:
            characters[character] = 1
    print(characters)
