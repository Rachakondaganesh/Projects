##SATELLITE IMAGE PROJECT
import random

import numpy as np
import scipy
import matplotlib.pyplot as plt
import imageio
import skimage
import warnings
warnings.filterwarnings('ignore')

#Creating a numpy array from an image file:
#Lets choose a WIFIRE satellite image file as an ndarray and display
#its type

from skimage import data
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
type(photo_data)

# let's see what is in this image
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()
# let's see the image data
print(photo_data)
print("SHAPE.",photo_data.shape)

# The shape of the ndarray show that it is a three layered matrix.
# The first two numbers here are length and width, and
# the third number (i.e. 3) is for three layers: Red, Green and Blue.

# RGB Color Mapping in the Photo:
# RED pixel indicates Altitude
# BLUE pixel indicates Aspect
# GREEN pixel indicates Slope
# The higher values denote higher altitude, aspect and slope.

photo_data.size # size of the data
photo_data.min(),photo_data.max() #minimum and maximum of the pixel
photo_data.mean() # average of the pixel

photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
photo_data[150,250]=0 # we wil set all 3 layers RGB(RED,GREEN,BLUE) to this
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

#Changing colors in a Range
#We can also use a range to change the pixel values. As an example,
# let us set the green layer for rows 200 to 800 to full intensity.
#We will set the value of Green layer to full intensity for rows 200
#(inclusive)
# to 800 (exclusive) for all the columns.

photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
photo_data[200:800,:,1]=255
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
photo_data[200:800 , :]=255
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

## AFTER DOING ABOVE TASK YOU CAN SEE THE WHITE BLOCK
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
photo_data[200:800 , :]=0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

#pick all pixels with low values
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
print("shape of the data",photo_data.shape)
low_value_filter=photo_data < 100
print("low value shape",low_value_filter.shape)
# Filtering Out Low Values:
#Whenever the low_value_filter is True, set value to 0.
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
photo_data[low_value_filter]=0
plt.figure(figsize=(10,10))
plt.imshow(low_value_filter)
plt.show()

#More Row and Column Operations
#We can design complex patterns by making columns a function
# of rows or vice-versa. Here we try a linear relationship between
#rows and columns.
rows_range=np.arange(len(photo_data))
print(rows_range)
cols_range=rows_range
print(cols_range)
print(type(rows_range))

#We are setting the selected rows and columns to the maximum value of
#255
photo_data[rows_range,cols_range]=255
print(photo_data)
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()
# we can see the diagonal white line

#Masking Images
#Now let us try to mask the image in shape of a circular disc.
total_rows,total_cols,total_layers=photo_data.shape
print("Photo data",photo_data.shape)
X,y=np.ogrid[:total_rows,:total_cols]
print("X = ",X.shape," and y=",y.shape)
from IPython.display import Image
Image("Images/figure.png")
center_row,center_col=total_rows /2 ,total_cols/2
print("CENTER ROW ",center_row ,"and CENTER COL",center_col)
#print(X - center_row)
#print(Y - center_col)
dist_from_center=(X-center_row)**2 +(y-center_col)**2
print("distance from center ",dist_from_center)
radius=(total_rows/2)**2
print("radius",radius)
circular_mask=(dist_from_center > radius)
print("circular mask",circular_mask)
print(circular_mask[1500:1700,2000:2200])
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
photo_data[circular_mask]=0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#Further Masking
#We can further improve the mask, for example just get upper half
#disc.
X,y=np.ogrid[:total_rows,:total_cols]
half_upper=X < center_row # this generates a mask for all rows above the center
half_upper_mask=np.logical_and(half_upper,circular_mask)
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
photo_data[half_upper_mask]=255
#photo_data[half_upper_mask]=random.randint(200,255)
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()


#Further Processing of our Satellite Imagery
#* Processing of RED Pixels

#* Remember that red pixels tell us about the height.
# Let us try to highlight all the high altitude areas. We will
#do this by detecting high intensity RED Pixels and muting down other areas.

#  DETECTING HIGH RED PIXELS
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
red_mask= photo_data[:,:,0]<150
photo_data[red_mask]=0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

# DETECTING HIGH GREEN PIXELS
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
green_mask=photo_data[:,:,1]<150
photo_data[green_mask]=0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

#DETECTING HIGH BLUE PIXELS
photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
blue_mask=photo_data[:,:,2]<150
photo_data[blue_mask]=0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

# Composite mask that takes thresholds on all three layers: RED, GREEN,
# BLUE

photo_data=imageio.imread("C:/Users/user/Downloads/satellite.image.png")
red_mask=photo_data[:,:,0]<150
green_mask=photo_data[:,:,1]>100
blue_mask=photo_data[:,:,2]<100
final_mask=np.logical_and(red_mask,green_mask,blue_mask)
photo_data[final_mask]=0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
plt.show()

## OUR SATELLITE PROJECT IS DONE ✅