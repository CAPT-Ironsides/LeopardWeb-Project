#Worked on by Cameron Avellani
import unittest
from test_instructor_class import test_instructor_class
#Create unit test class
class instructor_test(unittest.TestCase):

    def test_assemble(self):
        print("Assemble roster test has been called...")
        #Arrange
        self.ID = "000000"
        #Act
        result = test_instructor_class.test_assemble_roster(test_instructor_class, self.ID)
        #Assert
        self.assertEqual(result, 10)
    def test_print(self):
        print("Printing roster test has been called...")
        result = test_instructor_class.test_print_roster(test_instructor_class)
        self.assertEqual(result,10)
#envokes the unit test
if __name__ == "__main__":
    unittest.main()