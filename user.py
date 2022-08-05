import sqlite3
database = sqlite3.connect("data.db")
cursor = database.cursor()
class user:
    # Constructor
    def __init__(self, set_first, set_last, set_id):
        self.first_name = set_first
        self.last_name = set_last
        self.id = set_id

    # Method
    def set_first(self, name):
        self.first_name = name
    def set_last(self, name):
        self.last_name = name
    def set_id(self, num):
        self.id = num
    def show_first(self):
        return self.first_name
    def show_last(self):
        return self.last_name
    def show_id(self):
        return self.id
    def search_courses(self):
        sql_command = """SELECT * FROM COURSE"""
        return(sql_command)
    def search_by_parameters(self):
        print("What would you like to search for? (CRN, TITLE, DEPARTMENT, TIME, DAYS, SEMESTER, YEAR, CREDITS)")
        reply = input("")
        if (reply == "CRN") :
            answer = str(input("Enter an id: "))
            return(1, answer)
        elif (reply == "TITLE") :
            answer = str(input("Enter title: "))
            return(2, answer)
        elif (reply == "DEPARTMENT") :
            depart = str(input("Enter department: "))
            return (3, depart)
        elif (reply == "TIME") :
            time = str(input("Enter what time of day the class is: "))
            return (4, time)
        elif (reply == "DAYS") :
            days = str(input("Enter what days the class is: "))
            return (5, days)
        elif (reply == "SEMESTER") :
            semester = str(input("Enter semester of class: "))
            return (6, semester)
        elif (reply == "YEAR") :
            year = input("Enter year of class: ")
            if year.isnumeric():
                year = int(year)
            else:
                year = 0
            return (7, year)
        elif (reply == "CREDITS") :
            credits = input("Enter credits of class: ")
            if  credits.isnumeric():
                credits = int(credits)
            else:
                credits = 0
            return (8, credits)
        else:
            return (0, 0)

cursor.close()