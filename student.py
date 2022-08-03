import sqlite3
from user import user
database = sqlite3.connect("data.db")
cursor = database.cursor()
class student(user):
    # Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id

    # Method
    def add_courses(self, student_first, student_last, student_id):
        crn = str(input("Please type the CRN of the course you want to add.\n"))
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error adding the course to your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully added.\n")
            cursor.execute("""INSERT INTO STUDENT_COURSE VALUES(?, ?, ?, ?);""", (student_id, student_first, student_last, crn))
            database.commit()
    def remove_courses(self):
        crn = str(input("Please type the CRN of the course you want to remove.\n"))
        cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
        query_result = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error removing the course from your schedule. The CRN may not exist. Please try again.\n")
        else:
            print("Course successfully removed.\n")
            cursor.execute("""DELETE FROM STUDENT_COURSE WHERE COURSE_CRN = ?""", (crn,))
            database.commit()
    def print_schedule(self, id):
        cursor.execute("""SELECT STUDENT_COURSE.STUDENT_ID, COURSE.CRN, COURSE.TITLE, COURSE.DEPARTMENT, COURSE.TIME, COURSE.DAYS, COURSE.SEMESTER, COURSE.YEAR, COURSE.CREDITS
            FROM STUDENT_COURSE
            LEFT JOIN COURSE ON COURSE.CRN = STUDENT_COURSE.COURSE_CRN
            WHERE STUDENT_COURSE.STUDENT_ID = ?""", (id,))
        query_result = cursor.fetchall()
        print(query_result)