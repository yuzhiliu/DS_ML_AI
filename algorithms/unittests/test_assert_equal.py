import unittest

# https://stackoverflow.com/questions/17779526/python-nameerror-global-name-assertequal-is-not-defined
class TestTry(unittest.TestCase):
    def test_equal(self):
        self.assertAlmostEqual(0.1, 0.1000000000001)

if __name__ == '__main__':
    unittest.main()

