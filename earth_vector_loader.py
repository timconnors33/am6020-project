# https://pythongis.org/part2/chapter-06/nb/01-geodataframe.html

import geopandas as gpd
import matplotlib.pyplot as plt

data = gpd.read_file('d40c1024-82b3-418a-91cd-685c1824aafa.gdb')


print(type(data))
print(data.head())
print(data.info())

data.plot()

plt.show()