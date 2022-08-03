#Worked on by Cam Avellani
import sqlite3
from user import user

database = sqlite3.connect("data.db")
cursor = database.cursor()

class test_instructor_class(user):

    def test_assemble_roster(self, ID):
        test_value = 0
        cursor.execute("""SELECT * FROM STUDENT WHERE ID = ? """,(ID,))
        query_result = cursor.fetchall()

        if(len(query_result) == 0):
            print("There was an error adding the student to your roster. The ID may not exist. Please try again!\n")
        else:
            print("Student sucessfully added!\n")
            test_value = 10
        return(test_value)

    def test_print_roster(self):
        test_value = 0
        cursor.execute("""SELECT * FROM STUDENT""")
        test_value = 10
        return(test_value)
    #returns 10 if sucessful 0 if fail