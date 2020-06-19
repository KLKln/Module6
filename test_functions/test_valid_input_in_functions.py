import unittest
from more_functions import validate_input_in_functions as validate


class MyTestCase(unittest.TestCase):

    #self.assertEqual('HarHarHar', str_funcs.multiply_string('Har', 3))
    def test_score_input_test_name(self):
        self.assertEqual('Python Quiz: 0', validate.score_input('Python Quiz'))

    def test_score_input_test_score_valid(self):
        self.assertEqual('SQL Quiz: 89', validate.score_input('SQL Quiz', 89))

    def test_score_input_test_score_below_range(self):
        self.assertEqual(False, validate.score_input('SQL Quiz', -56))

    def test_score_input_test_score_above_range(self):
        self.assertEqual(False, validate.score_input('SQL Quiz', 199))

    def test_test_score_non_numeric(self):
        self.assertEqual(False, validate.score_input('SQL Quiz', 'lol'))


if __name__ == '__main__':
    unittest.main()
