from flask import *
from database import init_db, db_session
from models import *
from database import Base
from flask import redirect
from flask import Flask, jsonify

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "PPPPssssTTTT"

@app.route("/")
@app.route("/home")
def home():
    return render_template("landing.html")

@app.route("/all")
def all():
    opps=db_session.query(Event).all()
    return render_template("all.html", opps=opps)

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/elementary")
def elementary():
    opps = db_session.query(Event).where((Event.age_low <= 11)).all()
    return render_template("all.html", opps=opps)

@app.route("/middle")
def middle():
    opps = db_session.query(Event).where((Event.age_low <= 14)&(Event.age_high>= 12)).all()
    return render_template("all.html", opps=opps)

@app.route("/high")
def high():
    opps = db_session.query(Event).where((Event.age_low <= 18)&(Event.age_high>= 15)).all()
    return render_template("all.html", opps=opps)

@app.route("/online")
def online():
    opps = db_session.query(Event).where(Event.online == 1).all()
    return render_template("all.html", opps=opps)


@app.route("/in-person")
def in_person():
    opps = db_session.query(Event).where(Event.online == 0).all()
    return render_template("all.html", opps=opps)

@app.route("/camps")
def camps():
    opps = db_session.query(Event).where(Event.event_type=="camp").all()
    return render_template("all.html", opps=opps)

@app.route("/courses")
def courses():
    opps = db_session.query(Event).where(Event.event_type == "class").all()
    return render_template("all.html", opps=opps)

@app.route("/comps")
def comps():
    opps = db_session.query(Event).where(Event.event_type == "competition").all()
    return render_template("all.html", opps=opps)

# @app.route('/process-results', methods=['POST'])
# def process_results():
#     data = request.get_json()
#     answers = data['answers']
#     online = answers[0]["text"]
#     age=int(answers[1])
#     time_of_year = answers[2]
#     time_of_year2 = time_of_year["text"]
#     type_of_event = answers[3]
#     try:
#         type_of_event2 = answers[4]
#         try:
#             type_of_event3=answers[5]
#         except:
#             x=2
#     except:
#         x=1

#     posts=db_session.query(Event).all()
#     return redirect(url_for("all", opps=posts))

@app.route('/process-results', methods=['POST'])
def process_results():
    print(session["age"])
    opps=db_session.query(Event).all()
    return render_template("all.html", opps=opps)


@app.before_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
