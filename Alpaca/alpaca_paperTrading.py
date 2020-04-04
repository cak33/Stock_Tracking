import requests, json
from alpaca_config import *

# My Paper trading keys:
# APIKEY ID: PK29LGPVYXL0VWGZ0AIA
# Secret Key: s/jKYj5Yhy1z7zB3hZt2qzA9r7OltnGt1ao1LHPg

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