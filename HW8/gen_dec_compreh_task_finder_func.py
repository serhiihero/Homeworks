# Find all of the numbers from 1-1000 that have a 3 in them
custom_compr = [x for x in range(1, 1001) if '3' in str(x)]

if __name__ == '__main__':
    print(custom_compr)
