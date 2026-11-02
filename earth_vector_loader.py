# https://pythongis.org/part2/chapter-06/nb/01-geodataframe.html

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import matplotlib.image as img

data = gpd.read_file('d40c1024-82b3-418a-91cd-685c1824aafa.gdb')

print(type(data))
print(data.head())
print(data.info())

data.plot(linewidth=1, color='black')

plt.axis('off')
plt.savefig('ireland_coastline.png', dpi=600)

coastline_rgb = [0, 0, 0]
image = PIL.Image.open('ireland_coastline.png')
image = image.convert('RGB')

image_array = np.array(image)
coastline_y, coastline_x, coastline_rgb = np.where(image_array == coastline_rgb)

coastline_x = coastline_x.reshape(-1, 1)
coastline_y = coastline_y.reshape(-1, 1)
coastline_coords = np.concatenate((coastline_x, coastline_y), axis = 1)
coastline_coords = list(map(tuple, coastline_coords))
coastline_coords = sorted(tuple(set(coastline_coords)))


print(coastline_coords.__len__())