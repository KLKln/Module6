import unittest
from more_functions import validate_input_in_functions as validate


class MyTestCase(unittest.TestCase):

    def test_score_input_test_name(self):

        self.assertEqual('Kelly test 1', validate.score_input('Kelly test 1'))

    def test_score_input_test_score_valid(self):
        self.assertEqual('Kelly test 2', 95, validate.score_input('Kelly test 2', 95))

    def test_score_input_test_score_below_range(self):
        self.assertTrue(validate.score_input.test_score >= 0)

    def test_score_input_test_score_above_range(self):
        self.assertTrue(validate.score_input.test_score <= 100)


    def test_test_score_non_numeric(self):
        assert type(self) == int, 'Invalid test score, try again!'


if __name__ == '__main__':
    unittest.main()
