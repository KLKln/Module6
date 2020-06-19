"""
Program: validate_input_in_functions.py
Author: Kelly Klein
Last date modified: 6/17/2020
This program will .
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """
Use reST style.
:param test_name: input for name of test
:param test_score: score the student got on test
:param invalid_message:"invalid test score, try again!"
:return: test_name, test_score
raises keyError: raises an exception
"""
    while True:

        try:
            print("test_name is:", test_name)
            print("test_score is: ", test_score)
            print("invalid_message is:", invalid_message)
        except ValueError:
            raise ValueError(invalid_message)

        if int(test_score) < 0:
            return False
        elif int(test_score) > 100:
            return False
        else:
            test = (test_name + ':' + " " + str(test_score))

    # return { test_name: test_score}
        return test


if __name__ == '__main__':
    pass
