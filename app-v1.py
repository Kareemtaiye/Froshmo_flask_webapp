from flask import Flask, redirect, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

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
    
    #Register the student with their sport/
    REGISTRANTS[name] = sport

    #Redirect to re registrants page
    return redirect("/registrants")

@app.route("/registrants")
def reggistrants():
    name=request
    return render_template("registrants.html", registrants= REGISTRANTS)


# def home():

#     if request.method == "POST":
#          name = request.form.get("name")
#          return render_template("greet.html", name=name)
    
#     return render_template("index.html")

# @app.route('/greet', methods=["POST"])
# def greet():
#     name = request.form.get("name", "World")
#     return render_template("greet.html", name=name)

