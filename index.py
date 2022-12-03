from flask import Flask,jsonify
from flask_cors import CORS
app = Flask(__name__)


CORS(app)

@app.route('/')
def sendData():
    return jsonify([{
                        "country": "India",
                        "state": "Delhi"
                     },
                    {
                        "country": "USA",
                        "state": "Las Vegas"
                     },
                    {
                        "country": "India",
                        "state": "Mumbai"
                     },
                    {
                        "country": "Australia",
                        "state": "Adelaide"
                     },
                    {
                        "country": "New Zealand",
                        "state": "Victoria"
                     }
])