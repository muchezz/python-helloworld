from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Phase 6B Flask acceptance", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
