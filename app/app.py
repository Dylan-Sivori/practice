from flask import Flask
from dotenv import load_dotenv

name = "shaboiberries"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"Hello {name}"