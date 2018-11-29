import numpy as np
import cv2
import sys
import math

def distance(x, y, i, j):
    return np.sqrt((x-i)**2 + (y-j)**2)

def gaussian(x, sigma):
    return (1.0 / (2 * math.pi * (sigma ** 2))) * math.exp(- (x ** 2) / (2 * sigma ** 2))

def apply_bilateral_filter(flash, filtered_image, x, y, diameter, sigma_i, sigma_s):
    hl = diameter/2
    #print("diameter:"+str(diameter));
    i_filtered = 0
    Wp = 0
    i = 0
    while i < diameter:
        j = 0
        while j < diameter:
            neighbour_x = x - (hl - i)
            neighbour_y = y - (hl - j)
            if neighbour_x >= len(flash):
                neighbour_x -= len(flash)
            if neighbour_y >= len(flash[0]):
                neighbour_y -= len(flash[0])
            #print("x:"+str(x)+" h1:"+str(hl)+" nx:"+str(neighbour_x))
            #print("y:"+str(y)+" h1:"+str(hl)+" ny:"+str(neighbour_y))
            

            gi = gaussian(flash[int(neighbour_x)][int(neighbour_y)] - flash[x][y], sigma_i)
            gs = gaussian(distance(neighbour_x, neighbour_y, x, y), sigma_s)
            w = gi * gs
            i_filtered += flash[int(neighbour_x)][int(neighbour_y)] * w
            Wp += w
            j += 1
        i += 1
    i_filtered = i_filtered / Wp
    filtered_image[x][y] = int(round(i_filtered))
    
def bilateral_filter_own(flash, filter_diameter, sigma_i, sigma_s):
    filtered_image = np.zeros(flash.shape)
    i = 3
    while i < len(flash):
        j = 3
        print("current x"+str(i))
        while j < len(flash[0]):
            
            apply_bilateral_filter(flash, filtered_image, i, j, filter_diameter, sigma_i, sigma_s)
            j += 1
        i += 1
    return filtered_image

noFlash=cv2.imread('C:/Users/GIIIIIIINGEEEEEEE/Image Processing/test3a.jpg',cv2.IMREAD_COLOR)
flash=cv2.imread('C:/Users/GIIIIIIINGEEEEEEE/Image Processing/test3b.jpg',cv2.IMREAD_COLOR)
greyFlash=cv2.cvtColor( flash, cv2.COLOR_BGR2GRAY );
if (not flash is None) and (not noFlash is None):
    newImg=bilateral_filter_own(greyFlash,6,12.0,16.0);
    cv2.imshow("bilat",newImg);
    
