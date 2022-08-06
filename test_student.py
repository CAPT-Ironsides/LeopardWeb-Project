# Andrew worked on unit test for test student class
import unittest
from test_student_class import test_student_class

class StudentTest(unittest.TestCase):
    def test_add_course(self):
        print("Add Courses Test called...")
        # Arrange
        self.crn = "0000"                                                                  # CRN of a course that must be in the table
        # Act
        result = test_student_class.test_add_courses(test_student_class, self.crn)           # Executes test_student_class 
        # Assert
        self.assertEqual(result, 10)                                                         # Checks if the result is 10

if __name__ == "__main__":
    unittest.main()
