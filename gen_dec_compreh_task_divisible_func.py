# Find all of the numbers from 1-1000 that are divisible by 7

custom_compr = [x for x in range(1, 1001) if x % 7 == 0]

if __name__ == '__main__':
    print(custom_compr)
