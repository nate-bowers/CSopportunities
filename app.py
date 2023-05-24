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
    return render_template("about.html")

@app.before_request
def setup():
    init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
