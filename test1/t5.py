import unittest



class TwoTest(unittest.TestCase):
    def setUp(self):
        self.a = 100
        print('start')

    def test_one(self):
        print(self.a)
        print('第一次')

    def test_two(self):
        print(self.a)
        print('第二次')

    def tearDown(self):
        print('end')