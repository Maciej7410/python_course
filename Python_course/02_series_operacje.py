# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

np.random.seed(0)

A = np.random.randint(0, 10, 10)

series = pd.Series(A, name = 'los')

# %%

series.dtype
series.iloc[1]
series.iloc[-1]
series.index
series.name
series.shape

#%%

N = np.random.randn(10)
M = np.random.randn(10)

series_N = pd.Series(N)
series_M = pd.Series(M)

#%%

series_N.abs()
series_N.add(series_M)
series_N.subtract(series_M)
series_N.divide(series_M)

series.drop_duplicates()

series[4] = np.nan

series.dropna()

series.idxmax()   # max z serii
series.idxmin()   # min z serii

series.count()    # ilosc elementów z serii

series_N.cumsum() # sumuje pokolei tablicę na końcu suma całkowita
series_N.cummin() # kumlatywnie min w każdej rubryce min
series_N.cummax() # szuka największej w kulatywie
series_N.value_counts()

series.sum()
series.std() # odchylenie standardowe oblicza
series.describe()

# %%
hist_data = pd.Series(np.random.randn(10000))
hist_data.hist(bins=80)



# %%
top_3 = series_N.nlargest(3)