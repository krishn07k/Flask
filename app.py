from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)



@app.route('/')
@app.route('/home')
def home_page():
    student_details=contact_details()
    return render_template('home.html', student_details=student_details)



@app.route('/add', methods = ['GET' , 'POST'])
def add_stud():
    if request.method == 'GET':
        return render_template('addstud.html')
    else: 
        student_data=(
            request.form['name'],
            request.form['age']
        )
        insert_student(student_data)
        return render_template('add_succes.html')




def insert_student(student_data):
    connie=sqlite3.connect('student.db')
    c=connie.cursor()

    sql_string='INSERT INTO contact_details (Name,age) VALUES (?, ?)'
    c.execute(sql_string,student_data)
    
    connie.commit()
    connie.close()
    
    


def contact_details():
    connie=sqlite3.connect('student.db')
    c=connie.cursor()

    c.execute(""" SELECT * FROM contact_details""")

    student_details=c.fetchall()

    return student_details




if __name__ == "__main__":
    app.run()
