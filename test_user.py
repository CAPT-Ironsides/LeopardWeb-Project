# Andrew worked on unit test for log in and searching all courses
# James worked on the unit test for search course by parameter
import unittest
from test_user_class import test_user_class

class UserTest(unittest.TestCase):
    def test_login_student(self):
        print("Student Log In Test called...")
        # Arrange
        self.user_choice = 1
        self.first = "Andrew"
        self.last = "Lee"
        self.ID = "000000"
        self.password = "0"
        # Act
        result = test_user_class.test_login(test_user_class, self.user_choice, self.first, self.last, self.ID, self.password)
        # Assert
        self.assertEqual(result, 10)
    def test_login_instructor(self):
        print("Instructor Log In Test called...")
        # Arrange
        self.user_choice = 2
        self.first = "Daniel"
        self.last = "Bernoulli"
        self.ID = "1"
        self.password = "0"
        # Act
        result = test_user_class.test_login(test_user_class, self.user_choice, self.first, self.last, self.ID, self.password)
        # Assert
        self.assertEqual(result, 10)
    def test_login_admin(self):
        print("Admin Log In Test called...")
        # Arrange
        self.user_choice = 3
        self.first = "John"
        self.last = "Johnson"
        self.ID = "1"
        self.password = "0"
        # Act
        result = test_user_class.test_login(test_user_class, self.user_choice, self.first, self.last, self.ID, self.password)
        # Assert
        self.assertEqual(result, 10)
    def test_search_courses(self):
        print("Searching Course Test called...")
        # Arrange
        
        # Act
        result = test_user_class.test_search_courses(test_user_class)
        # Assert
        self.assertEqual(result, 10)
    def test_sbp(self):
        # Arrange
        self.crn = "6150"
        self.title = "MATH202"
        self.depart = "MATH"
        self.time = "8:00-10:00"
        self.days = "MWF"
        self.semester = "Fall"
        self.year = 2021
        self.credits = 3
        # Act
        result = test_user_class.test_sbp(test_user_class, self.crn, self.title, self.depart, self.time, self.days, self.semester, self.year, self.credits)
        # Assert
        self.assertEqual(result, 10)
if __name__ == "__main__":
    unittest.main()