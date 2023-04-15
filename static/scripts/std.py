# %%

import pandas as pd 
import numpy as np

mother = pd.Series(['N/A', 15, 22, 45, 31, -999, 21, 2, 0, 0, 0, 'broken'])
mother_replace = mother.replace({'N/A':np.nan, 'broken':np.nan, -999:np.nan})
mother_dropna = mother_replace.dropna()
# %%
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.std.html
# https://numpy.org/doc/stable/reference/generated/numpy.std.html

# numpy defaults to n
print(np.std(mother_replace))
print(np.std(mother_dropna))
# Make numpy use unbiased n-1
print(np.std(mother_replace, ddof=1))
print(np.std(mother_dropna, ddof=1))
# pandas defaults to unbiased n-1
print(mother_replace.std())
print(mother_dropna.std())

# pandas population standard devation
print(mother_replace.std(ddof=0))
print(mother_dropna.std(ddof=0))
