from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello world"
    return render_templates("index.html", greeting=greeting)

app.debug = True

if __name__ == "__main__":
    app.run()
