"""
Program: inner_functions.py
Author: Kelly Klein
Last date modified: 6/19/2020
This program will take 1 or two numbers and return the perimeter and area
"""


def measurements(a_list):
    """
    Use reST style.

    :param a_list:
    :return:
    """
    if len(a_list) == 1:
        side1 = a_list[0]
    elif len(a_list) == 2:
        side1 = a_list[0]
        side2 = a_list[1]

    def area(a_list):
        # argument can be 1 or 2 length list
        # how do I tell if it's a square? and can I do this based on length of list
        if len(a_list) == 1:
            return side1 * side1
        elif len(a_list) == 2:
            return side1 * side2

        # if square how do I calculate area of a square
        # A = side * side


    # argument can be 1 or 2 length list
    # how do I tell if it's a rectangle? and can I do this based on length of list
    # if recangle how do I calculate area of a square
    # A = (side1 + side1) + (side2 + side_2)

    def perimeter(a_list):
        if len(a_list) == 1:
            return side1 * 4
        elif len(a_list) == 2:
            return (side1 * 2) + (side2 * 2)


# assign variable to returned value from area
    per = perimeter(a_list)
# assign variable to returned value from perimeter
    are = area(a_list)



    return_string = ("Perimeter = ", per, "Area = ", are)
# "Perimeter = 14.0 Area = 12.25"
    return "Perimeter =", per, "Area =", are
