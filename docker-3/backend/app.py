import json
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, origins="*")
CORS(app)

@app.route('/api/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        [
            {"facebookUser": "aminespinoza10"},
            {"instagramUser": "aminespinoza10"},
            {"xUser": "aminespinoza"},
            {"linkedin": "amin-espinoza"},
            {"githubUser": "aminespinoza10"}
        ],
        "blog": "https://aminespinoza.com",
        "author": "Miranda Espinoza"
    }
    return json.dumps(value)