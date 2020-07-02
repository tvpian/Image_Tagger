# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 14:30:54 2020

@author: IMGADMIN
"""

import cv2
import numpy as np
import glob
import pandas as pd
import os
import numpy as np



# mouse callback function
data_path = os.getcwd()
files = glob.glob(data_path+"\\*.jpg")
img_counter=0
txt=[]
images=[]
pixels=[]
pixel_range=[]
real=[]
img=cv2.imread(files[img_counter])


#define the screen resulation
screen_res = 1280, 720
scale_width = screen_res[0] / img.shape[1]
scale_height = screen_res[1] / img.shape[0]
scale = min(scale_width, scale_height)
#resized window width and height
window_width = int(img.shape[1] * scale)
window_height = int(img.shape[0] * scale)

#cv2.WINDOW_NORMAL makes the output window resizealbe
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
#resize the window according to the screen resolution
cv2.resizeWindow('image', window_width, window_height)
def draw_circle(event,x,y,flags,param):
    global files
    global img_counter
    global img
    global pixel_range
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),10,(0,0,255),-1)
        pixel_range.append((x,y))
        print("Click Cordinates: ",x,y)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print("cleaned")
        #cv2.destroyAllWindows()
        pixel_range=[]
        img = np.zeros((512,512,3), np.uint8)
        img=cv2.imread(files[img_counter]) 
        cv2.imshow('image',img)
        #cv2.namedWindow('image')
        

# Create a black image, a window and bind the function to window
#img = np.zeros((512,512,3), np.uint8)

cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key == ord('n'):
        print("Next Image")
        txt=[]
        pixel_range=[]
        img_counter+=1
        if img_counter > len(files)-1:
            img_counter=len(files)-1
            print("Last Image") 
        img=cv2.imread(files[img_counter])
    elif key == ord('p'):
        print("Previous Image")
        txt=[]
        pixel_range=[]
        img_counter-=1
        if img_counter < 0:
            img_counter=0
            print("Last Image")
        img=cv2.imread(files[img_counter])
    elif key == ord('s'):
        print("saving entry")
        images.append(files[img_counter])
        pixels.append(pixel_range)
        real.append(float(text))        
    elif key == ord('0'):
        txt.append(0)
    elif key == ord('1'):
        txt.append(1)
    elif key == ord('2'):
        txt.append(2)
    elif key == ord('3'):
        txt.append(3)
    elif key == ord('4'):
        txt.append(4)
    elif key == ord('5'):
        txt.append(5)
    elif key == ord('6'):
        txt.append(6)
    elif key == ord('7'):
        txt.append(7)
    elif key == ord('8'):
        txt.append(8)
    elif key == ord('9'):
        txt.append(9)
    elif key == ord('.'):
        txt.append('.')
    elif key == ord('d'):
        try: 
            txt.pop()
        except:
            print("String is Empty")
        pixel_range
        img = np.zeros((512,512,3), np.uint8)
        img=cv2.imread(files[img_counter])    
    elif key == ord('s'):
        pass       
    text="".join(str(i) for i in txt)
    font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(img,text,(img.shape[0]-int(img.shape[0]/2),img.shape[1]-10), font, .5,(255,0,0),2,cv2.LINE_AA)
    cv2.putText(img,text,(window_height-int(window_height/2),window_width-10), font, 5,(255,0,0),2,cv2.LINE_AA)
        
        
cv2.destroyAllWindows()
final=pd.DataFrame({"Images":images,"Pixel_Range":pixels,"Real_Dim":real})
final.head()



def calc_pmr(pixels):
    real=29.5
    height0 = pixels[0]
    height1 = pixels[1]
    target0 = pixels[2]
    target1 = pixels[3]
    height_pixels = np.sqrt((height0[0] - height1[0])**2 + (height0[1] - height1[1])**2)
    target_pixels = np.sqrt((target0[0] - target1[0])**2 + (target0[1] - target1[1])**2)
    pmr= height_pixels/real
    target_real = target_pixels/pmr
    return target_real




x=map(calc_pmr,pixels)
set(x)




