PAPER_API_KEY = "PK29LGPVYXL0VWGZ0AIA"
PAPER_SECRET_KEY = "s/jKYj5Yhy1z7zB3hZt2qzA9r7OltnGt1ao1LHPg"

PAPER_HEADERS = {'APCA-API-KEY-ID': PAPER_API_KEY, 'APCA-API-SECRET-KEY': PAPER_SECRET_KEY}

BASE_URL = "https://paper-api.alpaca.markets"
HISTORICAL_URL = "https://data.alpaca.markets/v1"

ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)