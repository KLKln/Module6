import unittest
from more_functions import validate_input_in_functions as validate


class MyTestCase(unittest.TestCase):

    #self.assertEqual('HarHarHar', str_funcs.multiply_string('Har', 3))
    def test_score_input_test_name(self):
        self.assertEqual('Python Quiz: 0', validate.score_input('Python Quiz'+': 0'))

    def test_score_input_test_score_valid(self):
        self.assertEqual(validate.score_input(test_score=self) == int)

    def test_score_input_test_score_below_range(self):
        self.assertTrue(validate.score_input(test_score=self) >= 0)

    def test_score_input_test_score_above_range(self):
        self.assertTrue(validate.score_input(test_score=self) <= 100)


    def test_test_score_non_numeric(self):
        assert type(self) == int, 'Invalid test score, try again!'


if __name__ == '__main__':
    unittest.main()
