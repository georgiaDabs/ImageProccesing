import numpy as np
import cv2

windowName="Image";
img=cv2.imread('J:/image processing/dancingpumpkinguy.jpg', cv2.IMREAD_COLOR);
if not img is None:
    mask=np.ones((10,10),np.float)/100
    mask2=np.ones((5,5),np.float)/25
    blur=cv2.GaussianBlur(img, (15,15),0);
    grey=cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY);
    lapla=cv2.Laplacian(grey, cv2.CV_64F)
    filtered_img=cv2.filter2D(img,-1,mask)
    filtered_img2=cv2.filter2D(img,-1,mask)
    cv2.imshow(windowName,img);
    key=cv2.waitKey(0);
    if(key==ord('x')):
        cv2.destroyAllWindows();
        cv2.imshow(windowName,blur);
        key=cv2.waitKey(0);
        if(key==ord('c')):
            cv2.destroyAllWindows();
            cv2.imshow(windowName,grey);
            key=cv2.waitKey(0);
            if(key==ord('v')):
                cv2.destroyAllWindows();
                cv2.imshow(windowName,lapla);
else:
        print("no image file succesfully loadded.");
