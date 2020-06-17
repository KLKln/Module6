"""
Program: Hourly_Employee.py
Author: Kelly Klein
Last date modified: 6/16/2020
This program will take user input and return a String giving them the
    information, bad input will be handled.
"""


def hourly_employee_input():
    """this will take user input and print a string"""
    while True:
        try:
            name = input("Please enter your name: ")#get string of user input of name
            if name.isalpha():
                break
            else: raise TypeError
        except TypeError:
            print("Letters only, please.")
            continue
    while True:
        hours_worked = input("Please enter total hours worked: ")#get input and cast to int
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
        hourly_pay_rate = input("Please enter your hourly pay rate: ")#get user input and cast to float
        try:
            hourly_pay_rate = float(hourly_pay_rate)
            if hourly_pay_rate < 0:
                print("Negative numbers not allowed.")
                continue
            break
        except ValueError:
            print("Numbers only, please")
            continue


    print(name, "worked", hours_worked, "hours at", hourly_pay_rate, "dollars an hour.")#print a string including information
    #Kelly worked 40 hours at $25.00 and hour for a total(optional)


if __name__ == '__main__':
    hourly_employee_input()
