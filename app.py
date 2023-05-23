from flask import *
from database import init_db, db_session
from models import *
from database import Base

app = Flask(__name__)

# TODO: Change the secret key
app.secret_key = "PPPPssssTTTT"

@app.route("/")
@app.route("/home")
def home():
    return render_template("landing.html")

@app.route("/all")
def all():
    return render_template("allopps.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/about")
def about():
    #temp1= Event(name="iD Tech Summer Camps at Palo Alto High School", link="https://www.idtech.com/locations/california-summer-camps/palo-alto-high-school", summary="At iD Tech Summer Camps, students learn to code, design video games, produce videos, and more. This specific camp takes place at Palo Alto High School in California.", organization="iD Tech", price="~$1000 Prices Vary", online=False, location="Palo Alto High School, California", image_address="https://2018media.idtech.com/images/1571703681_loc-tuition-includes.jpg.webp?692ad5b218", age_high=17, age_low=7, event_type="camp", during_school_year=False)
    #db_session.add(temp1)
    #db_session.commit()
    return render_template("about.html")

@app.before_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
