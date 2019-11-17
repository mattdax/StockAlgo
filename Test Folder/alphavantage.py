import csv 
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='IYH3P1ZXYWIFM33F',output_format='csv')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL',interval = '60min',outputsize='full')

a  = []

reader = csv.reader(data,delimiter = ',')
for row in data:
	try:
		b = float(row[2]) + float(row[3]) + float(row[4])
		a.append(b/3)
	except ValueError:
		pass
print(a)