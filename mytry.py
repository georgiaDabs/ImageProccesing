import numpy as np
import cv2
import math
#import cv
from decimal import *
#open the no flash picture 
noFlash=cv2.imread('test3a.jpg',cv2.IMREAD_COLOR)
#open the flash picture
flash=cv2.imread('test3b.jpg',cv2.IMREAD_COLOR)
#variable of the intensity sigma
sigmaI=16
#variable of the distance sigma
sigmaD=12
#method for the gaussian function
def gaussian (dist,sigma):
    #work out the constant at the front of the equation
    const=1/(sigma*math.sqrt(2*math.pi))
    #work out the exponential
    toE=-(dist**2)/(sigma**2)
    #times the constant by e to the exponential
    g=(const)*(math.exp(toE))
    #return the result
    return g
#method to bilate an individual pixel taking in the coordinates, diameter around the pixel and which colour currently being done
def bilatOnPixel(x,y,diameter,channel):
    #work out the radius
    radius=int(diameter/2)
    #nx is the starting x
    nx=x-radius
    #the top E is numerator sum in the bilateral filter equation, instantiate to 0
    topE=0
    #the bottom E is denomenator sum in the bilateral filter equation, instantiate to 0
    bottomE=0
    #loop from x-radius to x+radius (i.e left to right)
    while(nx<(x+radius)):
        #loop from y-radius to y+radius (i.e top to bottom)
        ny=y-radius
        while(ny<(y+radius)):
            #work out the manhatten distance from the pixel being bilated
            distanceDiff=math.fabs(nx-x)+math.fabs(ny-y)
            #work out the intensity difference between the current pixel and the bilated pixel for the current channel
            intenseDiff=math.fabs(flash[x][y][channel]-flash[nx][ny][channel])
            #get the gaussian result for the distance difference 
            gDist=gaussian(distanceDiff, sigmaD)
            #get the gaussian result for the intensity difference
            gInt=gaussian(intenseDiff,sigmaI)
            #add to the the numerator the formula at this pixel
            topE+=gDist*gInt*noFlash[nx][ny][channel]
            #add to the numerator the formula at this pixel
            bottomE+=gDist*gInt
            #get the pixel above
            ny+=1
        #get the pixel on the left
        nx+=1
    #return the new result for the bilation of this pixel
    return topE/bottomE
#bilate on one of the image channels taking into account the neighbourhood
def bilate(diam,c):
    #make a new empty image full of zeroes
    newImg=np.zeros(noFlash.shape)
    #work out the radius
    radius=int(diam/2)
    #get the height, width and channels
    height,width,channels=noFlash.shape
    #loop through the xs of the pixels
    for x in range(0,height):
        #loop through the ys of the pixels
        for y in range(0,width):
            #if it is in the border just use the old pixel
             if((x<radius) or (x>(height-radius)) or (y<radius) or (y>(width-radius))):
                newImg[x][y]=noFlash[x][y][c]
            #otherwise bilate on the pixel
             else:
                newImg[x][y][c]=(bilatOnPixel(x,y,diam,c))
    #return the result
    return newImg
#show the original picture for comparison
cv2.imshow("OG image",noFlash)
#bilate on the green channel
greenFlash=bilate(10,1)
#bilate on the blue channel
blueFlash=bilate(10,0)
#bilate on the red channel
redFlash=bilate(10,2)
#save all the different channel results
cv2.imwrite("J:/image processingNEW/newGreenImg.jpg",greenFlash)
cv2.imwrite("J:/image processingNEW/newRedImg.jpg",redFlash)
cv2.imwrite("J:/image processingNEW/newBlueImg.jpg",blueFlash)
#get the height and width
height, width,channels=noFlash.shape
#make another new empty image
newImg=np.zeros(noFlash.shape)
#for each pixel recombine the three channels to get a coloured result
for x in range(0, height):
    for y in range(0,width):
        newImg[x][y][0]=blueFlash[x][y][0]
        newImg[x][y][1]=greenFlash[x][y][1]
        newImg[x][y][2]=redFlash[x][y][2]
#save the result
cv2.imwrite("J:/image processingNEW/newImg.jpg",newImg)


