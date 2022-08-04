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

# cursor.execute("ALTER TABLE INSTRUCTOR DROP PASSWORD")
# cursor.execute("ALTER TABLE INSTRUCTOR ADD PASSWORD TEXT DEFAULT '0'")

# cursor.execute("UPDATE ADMIN SET FIRST = 'George' WHERE FIRST = 'Geroge';")

#cursor.execute("UPDATE STUDENT SET ID = '100012' WHERE ID = '10012'")
#cursor.execute("UPDATE STUDENT_COURSE SET STUDENT_ID = '000001' WHERE STUDENT_ID = '1'")

cursor.execute("INSERT INTO INSTRUCTOR VALUES('7', 'John', 'Rambo', 'Full Prof.', '1982', 'BSCO', 'ramboj', 'BakerTeam1968');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('8', 'John', 'McClane', 'Full Prof.', '1988', 'BSEE', 'mcclanej', 'DieHard1988');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('9', 'Mike', 'Lowrey', 'Full Prof.', '1995', 'HUSS', 'lowreym', '1994Porsche911Turbo');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('10', 'Ethan', 'Hunt', 'Full Prof.', '1996', 'BSAS', 'hunte', 'CLASSIFIED');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('11', 'Kathryn', 'Railly', 'Full Prof.', '1995', 'HUSS', 'raillyk', 'TwelveMonkeys');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('12', 'Max', 'Rockatansky', 'Full Prof.', '1979', 'BSME', 'rockatanskym', 'BlackOnBlackV8');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('13', 'Millie', 'Rusk', 'Full Prof.', '2021', 'COMP', 'ruskm', 'ILoveBlueShirtGuy');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('14', 'Johnny', 'Utah', 'Full Prof.', '1991', 'BSEE', 'utahj', 'CopSurfer');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('15', 'Dominic', 'Toretto', 'Full Prof.', '2001', 'BSME', 'torettod', '1970DodgeChargerR/T');")
cursor.execute("INSERT INTO INSTRUCTOR VALUES('16', 'Sarah', 'Connor', 'Full Prof.', '1984', 'BCOS', 'connors', 'TechNoir');")


database.commit()
database.close()