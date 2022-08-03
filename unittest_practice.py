import unittest

def sum(a,b):
    return a + b

class Test(unittest.TestCase):
    def setUp(self):                                     # setUp function is called before each individual test is called
        print("SETUP Called...")
        self.a = 10
        self.b = 20
    def tearDown(self):                                 # tearDown function is called after each individual test is called
        print("TEARDOWN Called...")
        self.a = 0
        self.b = 0
    def test_sumfunc_1(self):                           # User created test #1
        print("TEST - 1 Called...")

        # Act
        result = sum(self.a,self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)
    def test_sumfunc_2(self):                           # User created test #2
        print("TEST - 2 Called...")

        # Act
        result = sum(self.b,self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)
if __name__ == "__main__":
    unittest.main()