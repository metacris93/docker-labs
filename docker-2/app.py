import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
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