import numpy as np
import cv2
windowName="Image";
img=cv2.imgRead('C:/Users/GIIIIIIINGEEEEEEE/Image Processing/dancingpumpkinheadguy.jpg', cv2.IMREAD_COLOR);
if not img is None:
    mask=np.ones((5,5),np.float)/25
    filtered_img=cv2.filter2D(img,-1,mask)
    cv2.imshow(windowName,filtered_img);
    key=cv2.waitKey(0);
    if(key==ord('x')):
        cv2.destroyAllWindows();
else:
        print("no image file succesfully loadded.");
