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
:param invalid_message:
:return: test_name, test_score
raises keyError: raises an exception
"""

    while True:
        test = input(test_name)
        test_name = test


        #test_score = int(input('please enter test score: '))
        #if 0 <= test_score <= 100:
            #return true
        #if 0 > test_score > 100:
            #return false
            #print(invalid_message)
        #break


    return
    #{test, test_score}
    pass

if __name__ == '__main__':
    pass
