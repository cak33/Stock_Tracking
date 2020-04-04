import requests, json

# My Paper trading keys:
# APIKEY ID: PK29LGPVYXL0VWGZ0AIA
# Secret Key: s/jKYj5Yhy1z7zB3hZt2qzA9r7OltnGt1ao1LHPg
'''
def get_historical_data(start, end):
	dates = {
		"start" = start
	}
	r = requests.get(HISTORICAL_URL, headers=PAPER_HEADERS)
	r = json.loads(r.content)

def get_account():
	r = requests.get(ACCOUNT_URL, headers=PAPER_HEADERS)
	return json.loads(r.content)

def create_order(symbol, qty, side, type, time_in_force):
	data = {
		"symbol": symbol,
		"qty": qty,
		"side": side,
		"type": type,
		"time_in_force": time_in_force

	}
	r = requests.post(ORDERS_URL, json=data, headers=PAPER_HEADERS)
	return json.loads(r.content)

def get_orders():
	r = requests.get(ORDERS_URL, headers=PAPER_HEADERS)
	return json.loads(r.content)

data = 
#response = create_order("TSLA", 100, "buy", "market", "gtc")
#print response

#orders = get_orders()
#print orders
'''
API_KEY = "69d22d5f25msh3ba5203e251f55bp1e24fbjsn87430ff5d1c9"
HISTORICAL_DATA_URL = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-historical-data"

HEADERS = {
	"x-rapidapi-host": "apidojo-yahoo-finance-v1.p.rapidapi.com",
	"x-rapidapi-key": API_KEY
}

payload = {
	"frequency": "1d",
	"filter": "history",
	"period1": "1546448400",
	"period2": "1546448402",
	"symbol": "AMRN"
}

response = requests.request("GET", HISTORICAL_DATA_URL, headers=HEADERS, params=payload)

f = open("json_data.txt", 'w')
#f.write(json.dumps(response, indent=4))
f.write(response.text)