"""
import csv 
from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key='IYH3P1ZXYWIFM33F',output_format='csv')
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL',interval = '2hr',outputsize='full')
"""

