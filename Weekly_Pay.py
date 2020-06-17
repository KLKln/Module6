"""
Program: Weekly_Pay.py
Author: Kelly Klein
Last date modified: 6/16/2020
This program will take user input and return values giving them the
    information, bad input will be handled, values printed to main.
"""


def weekly_pay(hours_worked, hourly_pay_rate):
    """
    use reST style.

    :param hours_worked: hours worked for the week
    :param hourly_pay_rate: pay per hour
    :returns: function that returns calculated weekly pay
    raises keyError: raises an exception
    """
    weekly_pay = hours_worked * hourly_pay_rate

    return weekly_pay


def hourly_employee_input():
    """
    use reST style.

    :param name: name of user
    :param hours_worked: hours worked for the week
    :param hourly_pay_rate: pay per hour
    :returns: function that returns calculated weekly pay
    raises keyError: raises an exception
    """
    while True:
        try:
            name = input("Please enter your name: ")  # get string of user input of name
            if name.isalpha():
                break
            else:
                raise TypeError
        except TypeError:
            print("Letters only, please.")
            continue
    while True:
        hours_worked = input("Please enter total hours worked: ")  # get input and cast to int
        try:
            hours_worked = int(hours_worked)
            if hours_worked < 0:
                print("Negative numbers not allowed.")
                continue
            break

        except ValueError:
            print("Numbers only, please.")
            continue

    while True:
        hourly_pay_rate = input("Please enter your hourly pay rate: ")  # get user input and cast to float
        try:
            hourly_pay_rate = float(hourly_pay_rate)
            if hourly_pay_rate < 0:
                print("Negative numbers not allowed.")
                continue
            break
        except ValueError:
            print("Numbers only, please")
            continue



    # print(name, "worked", hours_worked, "hours at", hourly_pay_rate, "dollars an hour.")
    # #print a string including information

    # assign the result to a variable
    # print result
    return name, weekly_pay(hours_worked, hourly_pay_rate)


if __name__ == '__main__':
    print(hourly_employee_input())  # assign the result to a variable
    # print result
