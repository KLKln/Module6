"""
Program: Multiply_String.py
Author: Kelly Klein
Last date modified: 6/17/2020
This program will take a String and a number and repeat
    the string n number of times.
"""

def multiply_string(message, n):
    """
    Use reST style.
    :param message: string message passed in
    :param n: number of times we repeat string
    :return: the string repeated n times
    raises keyError: raises an exception
    """

    multiplied_string = message * n

    return multiplied_string


if __name__ == '__main__':
    try:
        message = input('Please enter a String you would like repeated: ')
        n = int(input('How many times do you want to see it repeated? '))
    except ValueError as err:
        print("ValueError found!!")
    else:
        print(multiply_string(message, n))
