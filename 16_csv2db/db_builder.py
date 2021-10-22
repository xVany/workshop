# Team Name: Sleepy Programmers: Andy Lin, Shadman Rakib, Raymond Yeung
# SoftDev
# K16 -- Generating and accessing databses via Python (SQLITE)
# 2021-10-21

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

c.execute("CREATE TABLE roster(name TEXT, age INTEGER, userid INTEGER)")

with open('students.csv', newline='') as studentcsv:
    toRead = csv.DictReader(studentcsv)
    for student in toRead:
        c.execute("INSERT INTO roster VALUES (\""+student['name']+"\", "+student['age']+", "+student['id']+")")

c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)")

with open('courses.csv', newline='') as coursescsv:
    toRead = csv.DictReader(coursescsv)
    for course in toRead:
        c.execute("INSERT INTO courses VALUES (\""+course['code']+"\", "+course['mark']+", "+course['id']+")")

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
