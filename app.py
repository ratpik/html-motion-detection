from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def move():
    return render_template('move.html')

if __name__ == "__main__":
    app.run()


