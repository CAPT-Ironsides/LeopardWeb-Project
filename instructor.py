import sqlite3
from user import user
# database file connection 
database = sqlite3.connect("data.db") 
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
class instructor(user):
# Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id
    #Add courses to schedule
    def add_courses(self, instructor_id):
        crn = str(input("Please type the CRN of the course you want to add.\n"))
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error adding the course to your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully added.\n")
            cursor.execute("""INSERT INTO INSTRUCTOR_COURSE VALUES(?, ?);""", (instructor_id, crn))
            database.commit()
    #Removing courses from schedule
    def remove_courses(self):
        crn = str(input("Please type the CRN of the course you want to remove.\n"))
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error removing the course from your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully removed.\n")
            cursor.execute("""DELETE FROM INSTRUCTOR_COURSE WHERE COURSE_CRN = ?""", (crn,))
            database.commit()
    #Print course schedule
    def print_schedule(self, id):
        cursor.execute("""SELECT INSTRUCTOR_COURSE.INSTRUCTOR_ID, COURSE.CRN, COURSE.TITLE, COURSE.DEPARTMENT, COURSE.TIME, COURSE.DAYS, COURSE.SEMESTER, COURSE.YEAR, COURSE.CREDITS
            FROM INSTRUCTOR_COURSE
            LEFT JOIN COURSE ON COURSE.CRN = INSTRUCTOR_COURSE.COURSE_CRN
            WHERE INSTRUCTOR_COURSE.INSTRUCTOR_ID = ?""", (id,))
        query_result = cursor.fetchall()
        print(query_result)
    #Print roster
    def print_roster(self, id):
        crn = str(input("Please type the CRN of one of your courses.\n"))
        cursor.execute("""SELECT INSTRUCTOR_COURSE.COURSE_CRN, STUDENT_COURSE.STUDENT_ID, STUDENT_COURSE.STUDENT_FIRST, STUDENT_COURSE.STUDENT_LAST
            FROM INSTRUCTOR_COURSE
            LEFT JOIN STUDENT_COURSE ON STUDENT_COURSE.COURSE_CRN = INSTRUCTOR_COURSE.COURSE_CRN
            WHERE INSTRUCTOR_COURSE.INSTRUCTOR_ID = ? AND INSTRUCTOR_COURSE.COURSE_CRN = ?""", (id, crn))
        query_result = cursor.fetchall()
        print(query_result)

    # def assemble(self, id):
    #     ID = str(input("Enter a students W number (without the W) to add to your roster: "))
    #     cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (ID,))
    #     query_result = cursor.fetchall()
    #     if(len(query_result) == 0):
    #         print("There was an error adding the student to your roster. The W number may not exist. Please try again.\n")
    #     else:
    #         print("Student successfully added.\n")
