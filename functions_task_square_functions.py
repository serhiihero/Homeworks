# 2. Write a function square that takes 1 argument, the side of the square, and returns 3 values (using a tuple):
# the perimeter of the square, the area of the square, and the diagonal of the square.
from math import sqrt


def calc_sides_of_square(side_square_equals: int | float) -> int | float:
    calc_perimeter = (side_square_equals + side_square_equals) * 2
    cal_area = side_square_equals * side_square_equals
    calc_diagonal = side_square_equals * sqrt(2)
    return calc_perimeter, cal_area, calc_diagonal


if __name__ == '__main__':
    print(calc_sides_of_square(side_square_equals=4))
