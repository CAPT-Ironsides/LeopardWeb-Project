import sqlite3

database = sqlite3.connect("data.db")
cursor = database.cursor()

#cursor.execute("""DROP TABLE COURSE""");
# cursor.execute("""CREATE TABLE IF NOT EXISTS COURSE (
#     CRN TEXT PRIMARY KEY NOT NULL,
#     TITLE TEXT NOT NULL,
#     DEPARTMENT TEXT NOT NULL,
#     TIME TEXT NOT NULL,
#     DAYS TEXT NOT NULL,
#     SEMESTER TEXT NOT NULL,
#     YEAR INT NOT NULL,
#     CREDITS INT NOT NULL);""")

# cursor.execute("""INSERT INTO COURSE VALUES('0000', 'AppliedProgrammingConcepts', 'BSCO', '8:00AM-10:00AM', 'TR', 'Summer', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('1000', 'AdvancedCircuitDesign', 'BSEE', '10:00AM-12:00PM', 'MWF', 'Summer', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('2000', 'Thermodynamics', 'BSME', '12:00PM-2:00PM', 'TR', 'Fall', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('3000', 'IntroToProgramming', 'BSCO', '8:00AM-10:00AM', 'TRF', 'Spring', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('4000', 'ComputerArchitecture', 'BSEE', '3:00PM-5:00PM', 'MRF', 'Summer', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('5000', 'IntroToRobotics', 'BSAS', '11:00AM-1:00PM', 'WF', 'Fall', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('6000', 'LinearAlgebra', 'MATH', '8:00AM-10:00AM', 'MWF', 'Fall', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('6100', 'RealAnalysisI', 'MATH', '12:00PM-1:00PM', 'TR', 'Fall', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('6200', 'MachineLearning', 'MATH', '9:00AM-11:00AM', 'TR', 'Fall', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('6300', 'Probability&Statistics', 'MATH', '8:00AM-10:00AM', 'MWF', 'Fall', 2022, 4);""")
# cursor.execute("""INSERT INTO COURSE VALUES('6400', 'DiscreteMath', 'MATH', '8:00AM-10:00AM', 'MWF', 'Fall', 2022, 4);""")

sql_command = """INSERT INTO STUDENT VALUES('000000', 'Andrew', 'Lee', 2023, 'BSCO', 'leea');"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO COURSE VALUES('000000', 'Applied Programming Concepts', 'BSCO', '8:00AM-10:00AM', 'TR', 'Summer', 2022, 4);"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO ADMIN VALUES('000000', 'George', 'Washington', 'President', 'Dobbs 140', 'washingtong');"""
#cursor.execute(sql_command)
sql_command = """INSERT INTO INSTRUCTOR VALUES('1', 'John', 'Hancock', 'Prof', '2000', 'BSCO', 'hancockj');"""
#cursor.execute(sql_command)

cursor.execute("ALTER TABLE INSTRUCTOR DROP PASSWORD")
cursor.execute("ALTER TABLE INSTRUCTOR ADD PASSWORD TEXT DEFAULT '0'")

database.commit()
database.close()