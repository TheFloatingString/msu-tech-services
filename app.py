from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return "home"

@app.route("/saves")
def saves():
	return render_template("saves.html")

if __name__ == '__main__':
	app.run(debug=True)