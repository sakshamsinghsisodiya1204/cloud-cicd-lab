from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():

    return "Welcome to Cloud Computing Lab - CI/CD Version 1"

@app.route("/student")

def student():

    return {

        "name": "Student",

        "course": "Cloud Computing and DevOps",

        "experiment": "CI/CD Pipeline Using Jenkins"

    }

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
