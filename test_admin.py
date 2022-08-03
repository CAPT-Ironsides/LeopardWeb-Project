import unittest
from test_admin_class import test_admin_class

class AdminTest(unittest.TestCase):
    def test_add_course(self):
        print("Add Course Test called...")                                                # CRN of a course that must be in the table
        # Act
        result = test_admin_class.test_add_course(test_admin_class)           # Executes test_admin_class 
        # Assert
        self.assertEqual(result, 10)  # Checks if the result is 10
    def test_remove_course(self):
        print("Remove Course Test called...")                                                # CRN of a course that must be in the table
        # Act
        result = test_admin_class.test_remove_course(test_admin_class)           # Executes test_admin_class 
        # Assert
        self.assertEqual(result, 10)   
    def test_add_user(self):
        print("Add User Test called...")                                                # CRN of a course that must be in the table
        # Act
        result = test_admin_class.test_add_user(test_admin_class)           # Executes test_admin_class 
        # Assert
        self.assertEqual(result, 10) 
    def test_remove_user(self):
        print("Remove User Test called...")                                                # CRN of a course that must be in the table
        # Act
        result = test_admin_class.test_remove_user(test_admin_class)           # Executes test_admin_class 
        # Assert
        self.assertEqual(result, 10) 
    def test_add_student(self):
        print("Add Student Test called...")                                                # CRN of a course that must be in the table
        # Act
        result = test_admin_class.test_add_student(test_admin_class)           # Executes test_admin_class 
        # Assert
        self.assertEqual(result, 10) 
    def test_remove_student(self):
        print("Remove Student Test called...")                                                # CRN of a course that must be in the table
        # Act
        result = test_admin_class.test_remove_student(test_admin_class)           # Executes test_admin_class 
        # Assert
        self.assertEqual(result, 10) 

if __name__ == "__main__":
    unittest.main()
