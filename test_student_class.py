# Andrew worked on test student class
import sqlite3
from user import user
database = sqlite3.connect("data.db")
cursor = database.cursor()
class test_student_class(user):
    def test_add_courses(self, crn):
        #crn = input("Please type the CRN of the course you want to add.\n")
        test_value = 0
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error adding the course to your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully added.\n")
            test_value = 10
        return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not