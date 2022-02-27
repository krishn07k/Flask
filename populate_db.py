import sqlite3
connie=sqlite3.connect('student.db')

c = connie.cursor()

c.execute("""
    INSERT INTO contact_details (name,age) VALUES 
    ('krishna', 20),
    ('push' , 17)



  """ )


connie.commit()
connie.close()
