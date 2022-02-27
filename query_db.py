import sqlite3

connie=sqlite3.connect('student.db')

c=connie.cursor()

c.execute("""

SELECT * FROM contact_details

""")

student_info=c.fetchall()

for student in student_info:
    print(student)

connie.commit()
connie.close()