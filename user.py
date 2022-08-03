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
        print("Enter a value to show course.")
        crn = str(input("Enter an id: "))
        title = str(input("Enter title: "))
        depart = str(input("Enter department: "))
        time = str(input("Enter what time of day the class is: "))
        days = str(input("Enter what days the class is: "))
        semester = str(input("Enter semester of class: "))
        year = input("Enter year of class: ")
        credits = input("Enter credits of class: ")
        if year.isnumeric() and credits.isnumeric():
            year = int(year)
            credits = int(credits)
        else:
            year = 0
            credits = 0
        return(crn, title, depart, time, days, semester, year, credits)
cursor.close()