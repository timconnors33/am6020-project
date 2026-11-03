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

def count_coastline(image, x_min, x_max, y_min, y_max, coastline_rgb):
    
    image = image.convert('RGB')                
    image = crop_image(image, x_min, x_max, y_min, y_max)
    image.show()

    image_array = np.array(image)
    coastline_y, coastline_x, coastline_rgb = np.where(image_array == coastline_rgb)

    coastline_x = coastline_x.reshape(-1, 1)
    coastline_y = coastline_y.reshape(-1, 1)
    coastline_coords = np.concatenate((coastline_x, coastline_y), axis = 1)
    coastline_coords = list(map(tuple, coastline_coords))
    coastline_coords = sorted(tuple(set(coastline_coords)))

    return coastline_coords.__len__()



def crop_image(image, x_min, x_max, y_min, y_max):
    image = image.crop((x_min, y_min, x_max, y_max))
    return image

data.plot(linewidth=1, color='black')

plt.axis('off')
plt.savefig('ireland_coastline.png', dpi=600)
image = PIL.Image.open('ireland_coastline.png')

print(count_coastline(image, 0, image.width / 2, 0, image.height / 2, [0, 0, 0]))