from alpha_vantage.timeseries import TimeSeries
import csv
API_KEY = "JLMZNQVDC3F14K55"
ts = TimeSeries(key='API_KEY', output_format='csv')
data, meta_data = ts.get_daily_adjusted(symbol='MSFT', outputsize='full')

f = open("json_data.csv", 'w')

writer = csv.writer(f)
writer.writerows(data)
