# Andrew worked on log in and search course methods for test user class
# James worked on the search course by parameter method
import sqlite3
from user import user
database = sqlite3.connect("data.db")
cursor = database.cursor()
class test_user_class(user):
    def test_search_courses(self):
        test_value = 0
        cursor.execute("""SELECT * FROM COURSE""")
        test_value = 10
        return(test_value)
    def test_sbp(self, crn, title, depart, time, days, semester, year, credits): 
       cursor.execute("""INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (crn, title, depart, time, days, semester, year, credits))
       test_value = 0
       cursor.execute("""SELECT * FROM COURSE WHERE (CRN = ? AND TITLE = ? AND DEPARTMENT = ? AND TIME = ? AND DAYS = ? AND SEMESTER = ? AND YEAR = ? AND CREDITS = ?)""" , (crn, title, depart, time, days, semester, year, credits))
       query_result = cursor.fetchall()
       if(len(query_result) == 0):
           print("There was an error finding the course in the system.\n")
       else:
           print("Course successfully found.\n")
           test_value = 10
       cursor.execute("""DELETE FROM COURSE WHERE CRN = ?;""", (crn,))
       return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not
    def test_login(self, user_choice, first, last, id, password):
        #first = input("Enter your first name: \n")
        #last = input("Enter your last name: \n")
        #id = str(input("Enter your ID without the W: \n"))
        #password = input("Enter your password: \n")
        if(user_choice == 1):
            # Verify student credentials
            cursor.execute("""SELECT ID FROM STUDENT WHERE ID = ?""", (id,))
            query_result1 = cursor.fetchall()
            cursor.execute("""SELECT FIRST FROM STUDENT WHERE FIRST = ?""", (first,))
            query_result2 = cursor.fetchall()
            cursor.execute("""SELECT LAST FROM STUDENT WHERE LAST = ?""", (last,))
            query_result3 = cursor.fetchall()
            cursor.execute("""SELECT PASSWORD FROM STUDENT WHERE PASSWORD = ?""", (password,))
            query_result4 = cursor.fetchall()
            
        elif(user_choice == 2):
            # Verify instructor credentials
            cursor.execute("""SELECT ID FROM INSTRUCTOR WHERE ID = ?""", (id,))
            query_result1 = cursor.fetchall()
            cursor.execute("""SELECT FIRST FROM INSTRUCTOR WHERE FIRST = ?""", (first,))
            query_result2 = cursor.fetchall()
            cursor.execute("""SELECT LAST FROM INSTRUCTOR WHERE LAST = ?""", (last,))
            query_result3 = cursor.fetchall()
            cursor.execute("""SELECT PASSWORD FROM INSTRUCTOR WHERE PASSWORD = ?""", (password,))
            query_result4 = cursor.fetchall()

        elif(user_choice == 3):
            # Verify admin credentials
            cursor.execute("""SELECT ID FROM ADMIN WHERE ID = ?""", (id,))
            query_result1 = cursor.fetchall()
            cursor.execute("""SELECT FIRST FROM ADMIN WHERE FIRST = ?""", (first,))
            query_result2 = cursor.fetchall()
            cursor.execute("""SELECT LAST FROM ADMIN WHERE LAST = ?""", (last,))
            query_result3 = cursor.fetchall()
            cursor.execute("""SELECT PASSWORD FROM ADMIN WHERE PASSWORD = ?""", (password,))
            query_result4 = cursor.fetchall()
            
        else:
            print("That was not a valid input. Please try again.\n")
            result_first = "er404"
            result_last = "er404"
            result_id = "er404"
            result_password = "er404"

        if(len(query_result1) == 0):
            result_id = "er404"
        else:
            result_id = id
        if(len(query_result2) == 0):
            result_first = "er404"
        else:
            result_first = first
        if(len(query_result3) == 0):
            result_last = "er404"
        else:
            result_last = last
        if(len(query_result4) == 0):
            result_password = "er404"
        else:
            result_password = password

        # Successful Log In
        if(first == result_first) and (last == result_last) and (id == result_id) and (password == result_password):
            test_value = 10     # Returns 10 if log in successful, returns 0 if not
        return(test_value)