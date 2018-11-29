import numpy as np
import cv2

flash=cv2.imread('C:/Users/GIIIIIIINGEEEEEEE/Image Processing/test3b.jpg',cv2.IMREAD_COLOR)
greyFlash=cv2.cvtColor( flash, cv2.COLOR_BGR2GRAY );
x=50
y=50
print(greyFlash[x][y]-greyFlash[x-1][y-1])
