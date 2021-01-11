# Import initial libraries
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import plotly.graph_objs as go

# Date Ranges for SP 500 and for all tickers
# Modify these date ranges each week.
# The below will pull back stock prices from the start date until end date specified.
start_sp = datetime.datetime(2013, 1, 1)
end_sp = datetime.datetime(2018, 3, 9)
# This variable is used for YTD performance.
end_of_last_year = datetime.datetime(2017, 12, 29)
# These are separate if for some reason want different date range than SP.
stocks_start = datetime.datetime(2013, 1, 1)
stocks_end = datetime.datetime(2018, 3, 9)

# Leveraged from the helpful Datacamp Python Finance trading blog post.
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
#yf.pdr_override() # <== that's all it takes :-)
sp500 = pdr.get_data_yahoo('^GSPC', 
                           start_sp,
                             end_sp)
    
print(sp500)