import unittest
import unittest as mock
from more_functions import string_functions as str_funcs

class MyTestCase(unittest.TestCase):

    def test_call_with_value(self):

        self.assertEqual('HarHarHar', str_funcs.multiply_string('Har', 3))
        self.assertEqual('RadicalRadicalRadical', str_funcs.multiply_string('Radical', 3))
        self.assertEqual('GnarlyGnarlyGnarlyGnarly', str_funcs.multiply_string('Gnarly', 4))
        self.assertEqual('HaHaHaHaHaHaHaHaHa', str_funcs.multiply_string('Ha', 9))


if __name__ == '__main__':
    unittest.main()
