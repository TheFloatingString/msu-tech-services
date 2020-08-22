def parse_url(SHEET_ID, API_KEY):
	return "https://sheets.googleapis.com/v4/spreadsheets/"+SHEET_ID+"/values/Form%20responses%201!A1:G100?key="+API_KEY
