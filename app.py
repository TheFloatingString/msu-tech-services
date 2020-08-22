from flask import Flask, render_template
import requests
import os

from src.functions import parse_url

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/saves")
def saves():
	return render_template("saves.html")

@app.route("/api/get_questions")
def getQuestions():


	SHEET_ID = os.getenv("SHEET_ID") 
	API_KEY = os.getenv("API_KEY") 

	URL = parse_url(SHEET_ID, API_KEY)

	response_dict = requests.get(URL).json()

	parameters = response_dict["values"][0]

	processed_dict = dict()
	processed_dict["data"] = list()

	for content_row in response_dict["values"][1:-1]:
		row_dict = dict()
		for index in range(len(content_row)):
			row_dict[parameters[index]] = content_row[index]
		processed_dict["data"].append(row_dict)

	return processed_dict

if __name__ == '__main__':
	app.run(debug=True)