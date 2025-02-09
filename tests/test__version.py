import unittest
import dsa

class TestVersion(unittest.TestCase):
    def test_version(self):
        print('\nVersion Number')
        print(dsa.version)
        print(dsa.__version__)

if __name__ == '__main__':
    unittest.main()
