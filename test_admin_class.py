import sqlite3
from user import user
database = sqlite3.connect("data.db")
cursor = database.cursor()
class test_admin_class(user):

    def test_add_course(self): 
       crn = "6150"
       title = "MATH202"
       depart = "MATH"
       time = "8:00-10:00"
       days = "MWF"
       semester = "Fall"
       year = 2021
       credits = 3
       cursor.execute("""INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (crn, title, depart, time, days, semester, year, credits))
       test_value = 0
       cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
       query_result = cursor.fetchall()
       if(len(query_result) == 0):
           print("There was an error adding the course to the system.\n")
       else:
           print("Course successfully added to system.\n")
           test_value = 10
       cursor.execute("""DELETE FROM COURSE WHERE CRN = ?;""", (crn,))
       return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not
    
    def test_remove_course(self):
       test_value = 0
       crn = "6150"
       title = "MATH202"
       depart = "MATH"
       time = "8:00-10:00"
       days = "MWF"
       semester = "Fall"
       year = 2021
       credits = 3
       cursor.execute("""INSERT INTO COURSE VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", (crn, title, depart, time, days, semester, year, credits))
       cursor.execute("""DELETE FROM COURSE WHERE CRN = ?;""", (crn,))
       cursor.execute("""SELECT * FROM COURSE WHERE CRN = ?""", (crn,))
       query_result = cursor.fetchall()
       if(len(query_result) != 0):
           print("There was an error removing the course. The CRN may not exist. Please try again.\n")
       else:
           print("Course successfully added.\n")
           test_value = 10
       return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not

    def test_add_user(self):
      test_value = 0
      uid = "212"
      fname = "Paul"
      lname = "Walker"
      title = "Driver"
      office = "Heaven"
      email = "paulydubs@gmail.com"
      cursor.execute("""INSERT INTO ADMIN VALUES(?, ?, ?, ?, ?, ?);""", (uid, fname, lname,title, office,email))
      cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?""", (uid,))
      query_result = cursor.fetchall()
      if(len(query_result) == 0):
           print("There was an error adding the user to admin.\n")
      else:
           print("Admin successfully added to system.\n")
           test_value = 10
      #cursor.execute("""DELETE * FROM ADMIN WHERE ID = ?""", (uid,))

      return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not
    
    def test_remove_user(self):
      test_value = 0
      uid = "212"
      fname = "Paul"
      lname = "Walker"
      title = "Driver"
      office = "Heaven"
      email = "paulydubs@gmail.com"
      #cursor.execute("""INSERT INTO ADMIN VALUES(?, ?, ?, ?, ?, ?);""", (uid, fname, lname,title, office,email))
      cursor.execute("""DELETE FROM ADMIN WHERE ID = ?""", (uid,))
      cursor.execute("""SELECT * FROM ADMIN WHERE ID = ?""", (uid,))
      query_result = cursor.fetchall()
      if(len(query_result) != 0):
           print("There was an error removing the user to admin.\n")
      else:
           print("Admin successfully removed from system.\n")
           test_value = 10
      cursor.execute("""DELETE FROM ADMIN WHERE ID = ?""", (uid,))

      return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not

    def test_add_student(self):
      test_value = 0
      uid = "2323"
      fname = "Carlo"
      lname = "Wentz"
      grad = "2023"
      major = "BSCO"
      email = "wentzc@wit.edu"
      cursor.execute("""INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?);""", (uid, fname, lname, grad,major,email))
      cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (uid,))
      query_result = cursor.fetchall()
      if(len(query_result) == 0):
           print("There was an error adding the user to Student.\n")
      else:
           print("Student successfully added to system.\n")
           test_value = 10
      #cursor.execute("""DELETE * FROM STUDENT WHERE ID = ?""", (uid,))
      return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not
    
    def test_remove_student(self):
            test_value = 0
            uid = "2323"
            fname = "Carlo"
            lname = "Wentz"
            grad = "2023"
            major = "BSCO"
            email = "wentzc@wit.edu"
            #cursor.execute("""INSERT INTO STUDENT VALUES(?, ?, ?, ?, ?, ?);""", (uid, fname, lname, grad,major,email))
            cursor.execute("""DELETE FROM STUDENT WHERE ID = ?""", (uid,))
            cursor.execute("""SELECT * FROM STUDENT WHERE ID = ?""", (uid,))
            query_result = cursor.fetchall()
            if(len(query_result) != 0):
                print("There was an error removing the user from Student.\n")
            else:
                print("Student successfully removed from system.\n")
                test_value = 10
            return(test_value)      # Returns 10 if a course is successfully added, returns 0 if not
    