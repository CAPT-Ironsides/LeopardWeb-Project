import sqlite3
from datetime import datetime
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
        cursor.execute("""SELECT COURSE.START_TIME FROM COURSE WHERE CRN = ?""", (crn,))
        start = cursor.fetchall()
        cursor.execute("""SELECT COURSE.END_TIME FROM COURSE WHERE CRN = ?""", (crn,))
        end = cursor.fetchall()
        cursor.execute("""SELECT COURSE.DAYS FROM COURSE WHERE CRN = ?""", (crn,))
        days = cursor.fetchall()
        cursor.execute("""SELECT COURSE.SEMESTER FROM COURSE WHERE CRN = ?""", (crn,))
        semester = cursor.fetchall()
        cursor.execute("""SELECT COURSE.YEAR FROM COURSE WHERE CRN = ?""", (crn,))
        year = cursor.fetchall()
        if(len(query_result) == 0):
            print("There was an error adding the course to your schedule. The CRN may not exist. Please try again.\n")
        else:
            # Grab all start times
            cursor.execute("""SELECT COURSE.START_TIME
                    FROM STUDENT_COURSE
                    LEFT JOIN COURSE ON COURSE.CRN = STUDENT_COURSE.COURSE_CRN
                    WHERE STUDENT_COURSE.STUDENT_ID = ?""", (student_id,))
            start_times = cursor.fetchall()
            # Grab all end times
            cursor.execute("""SELECT COURSE.END_TIME
                    FROM STUDENT_COURSE
                    LEFT JOIN COURSE ON COURSE.CRN = STUDENT_COURSE.COURSE_CRN
                    WHERE STUDENT_COURSE.STUDENT_ID = ?""", (student_id,))
            end_times = cursor.fetchall()
            # Grab all days, semesters, and years
            cursor.execute("""SELECT COURSE.DAYS, COURSE.SEMESTER, COURSE.YEAR
                    FROM STUDENT_COURSE
                    LEFT JOIN COURSE ON COURSE.CRN = STUDENT_COURSE.COURSE_CRN
                    WHERE STUDENT_COURSE.STUDENT_ID = ?""", (student_id,))
            query_courses = cursor.fetchall()

            # Check course conflicts
            for i in range(0, len(start_times)):
                #print(start_times[i][0])
                if(datetime.strptime(str(start[0][0]), '%I:%M %p') < datetime.strptime(str(end_times[i][0]), '%I:%M %p') and datetime.strptime(str(end[0][0]), '%I:%M %p') > datetime.strptime(str(start_times[i][0]), '%I:%M %p')):
                    if(days[0][0] == query_courses[i][0] or (semester[0][0] == query_courses[i][1] and year[0][0] == query_courses[i][2])):
                        print("\nCourse time conflicts with another course!\n")
                        return None
                
            cursor.execute("""INSERT INTO STUDENT_COURSE VALUES(?, ?, ?, ?);""", (student_id, student_first, student_last, crn))
            database.commit()
            print("Course successfully added.\n")
            
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
        cursor.execute("""SELECT STUDENT_COURSE.STUDENT_ID, COURSE.CRN, COURSE.TITLE, COURSE.DEPARTMENT, COURSE.START_TIME, COURSE.END_TIME, COURSE.DAYS, COURSE.SEMESTER, COURSE.YEAR, COURSE.CREDITS
            FROM STUDENT_COURSE
            LEFT JOIN COURSE ON COURSE.CRN = STUDENT_COURSE.COURSE_CRN
            WHERE STUDENT_COURSE.STUDENT_ID = ?""", (id,))
        query_result = cursor.fetchall()
        print(query_result)