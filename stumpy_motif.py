# https://stumpy.readthedocs.io/en/latest/Tutorial_The_Matrix_Profile.html
# https://seanlaw.github.io/2019/05/13/stumpy/
# requires python3
import stumpy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("DATASET.CSV")
your_time_series = df.Close
window_size = 120  # Approximately, how many data points might be found in a pattern

matrix_profile = stumpy.stump(your_time_series, m=window_size)
print (matrix_profile)
# array of [[min_distance_score, index], ...]

df["Mp"] = np.concatenate([matrix_profile[:, 0], np.array([0]*(window_size-1))])
# matrix_profile[:, 0]
df[["Close", "Mp"]].plot(logy=True) # , sharex=True)
# df[["Close"]].plot(logy=True)
# df[["Mp"]].plot()

plt.show()


if False:
    # https://stumpy.readthedocs.io/en/latest/Tutorial_STUMPY_Basics.html
    import ssl, io, urllib
    import stumpy
    import pandas as pd
    import numpy as np

    colnames = ['drum pressure',
                'excess oxygen',
                'water level',
                'steam flow'
            ]

    context = ssl.SSLContext()  # Ignore SSL certificate verification for simplicity
    url = 'https://www.cs.ucr.edu/~eamonn/iSAX/steamgen.dat'
    raw_bytes = urllib.request.urlopen(url, context=context).read()
    data = io.BytesIO(raw_bytes)
    steam_df = pd.read_csv(data, header=None, sep="\s+")
    steam_df.columns = colnames
    print (steam_df.head())

    '''
    series = [float(x) for x in [1, 2, 5, 0, 3, 5, 1, 7, 8, 1, 2, 5]]
    steam_df = pd.DataFrame({"steam flow": series})
    m = 3
    '''
    m = 640
    mp = stumpy.stump(steam_df['steam flow'], m)
