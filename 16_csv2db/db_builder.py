# Team Name: Sleepy Programmers: Andy Lin, Shadman Rakib, Raymond Yeung
# SoftDev
# K16 -- Creating and adding to a SQLite database via Python
# 2021-10-20

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute("CREATE TABLE roster(name TEXT, age INTEGER, userid INTEGER)") # create student table in database
# formatting: string name, int age, int userid

with open('students.csv', newline='') as studentcsv:
    toRead = csv.DictReader(studentcsv)
    for student in toRead:
        c.execute("INSERT INTO roster VALUES (\""+student['name']+"\", "+student['age']+", "+student['id']+")")
        # for each row in csv, insert the row data into the data (same order as original table)
        # also first row gets ignored as they are the headers
c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")
# formatting: string code, int mark, int id

with open('courses.csv', newline='') as coursescsv: # create course table in database
    toRead = csv.DictReader(coursescsv)
    for course in toRead:
        c.execute("INSERT INTO courses VALUES (\""+course['code']+"\", "+course['mark']+", "+course['id']+")")
        # for each row in csv, insert the row data into the data (same order as original table)
        # also first row gets ignored as they are the headers
        
command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


