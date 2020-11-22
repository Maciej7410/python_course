# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# %%
stock_price = {'Apple':196,'CD Project':215,'Amazon':1833}
stock_price_series = pd.Series(stock_price, name='price')

stock_price_array = stock_price_series.values

stock_price_array_series = pd.Series(stock_price_array)

apple_price = stock_price_series['Apple']

'Apple' in stock_price_series

#%%

np.random.seed(0)

A = np.random.random(20)
s = pd.Series(A)

s[5:10]
s[:10]