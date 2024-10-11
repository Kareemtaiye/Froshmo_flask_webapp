from flask import Flask, redirect, render_template, request
import sqlite3
from db_abst import db

app = Flask(__name__)

conn = db.db_connect("students.db")

cursor = conn.cursor()

insert_query = '''
    INSERT INTO students (name, sport)
    VALUES (?, ?)
'''

select_query = '''
    SELECT * FROM students
'''

delete_query = '''
    DELETE FROM students WHERE id = ?
'''


SPORTS = ["Basketball", "Soccer", "Volleyball"]

@app.route("/", methods=["GET", "POST"])
def home():

    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    sport = request.form.get("sport")

    #Validate student's name
    if not name:
        return render_template('error.html', message="Missing name")
    
    #Validate student's sport
    if not sport:
        return render_template("error.html", message="Missing sport")

    #Check for bogus or invalid school sport
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid sport")
    
    #Register the student with their sport in the database
    cursor.execute(insert_query, (name, sport))
    conn.commit()

    #Redirect to re registrants page
    return redirect("/registrants")

@app.route("/registrants")
def reggistrants():
    query = cursor.execute(select_query)
    registrants = query.fetchall()
    aa = []
    for reg in registrants:
        aa.append(reg)
    print(registrants)

    return render_template("registrants-v2.html", registrants=aa)

@app.route('/deregister', methods=["POST"])
def deregister():
    
    reg_id = request.form.get("id")
    if not reg_id:
        return render_template("failure.html", message="No or Invalid id")
    
    cursor.execute(delete_query, (reg_id,))
    conn.commit()
    return redirect("/registrants")