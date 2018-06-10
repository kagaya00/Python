



"""

Histograms
Histograms can be plotted using the plot.hist() method. We can specify number of bins.



"""


import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.plot.hist(bins=20)
