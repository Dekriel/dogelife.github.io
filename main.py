from flask import *
import json


app = Flask(__name__)

@app.route("/")
def homepage():
    with open("settings.json", 'r') as f:
        contents = json.loads(f.read())
    if contents["has_character"] == "False":
        return render_template("main_prompt.html")


@app.route("/howto")
def howto():
    return render_template("how_to.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route('/static/<name>')
def get_file(name):
    with open(f"static/{name}", "rb") as f:
        return f.read()

@app.route('/templates/<name>')
def script(name):
    with open(f"templates/{name}", "r") as f:
        return f.read()

@app.route('/rng')
def rng():
    return render_template('rng.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
