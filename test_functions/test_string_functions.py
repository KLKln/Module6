import unittest
import unittest as mock
from more_functions import string_functions as str_funcs

class MyTestCase(unittest.TestCase):

    def test_call_with_value(self):
        self.assertEqual('AyahAyahAyah', str_funcs.multiply_string('Ayah', 3))


if __name__ == '__main__':
    unittest.main()
