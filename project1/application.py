import os

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))



# Application routea 

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@app.route("/login", methods=['GET'])
def login():
    return render_template("login.html")

@app.route("/logout", methods=['GET'])
def logout():
    return render_template("login.html")

@app.route("/import", methods=['GET'])
def import_file():
    return render_template("import.html")

@app.route("/search", methods=['GET'])
def search():
    return render_template("search.html")

@app.route("/book", methods=['GET'])
def book():
    return render_template("book.html")

# APIs for fetching and posting review
@app.route("/review", methods=['POST'])
def review():
    return "book.html"

@app.route("/googlereads_review", methods=['GET'])
def googlereads_review():
    return "book.html"

@app.route("/api/v1/<isbn>", methods=['GET'])
def api_v1():
    return "book.html"
    
    

