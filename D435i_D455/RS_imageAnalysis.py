import pyrealsense2
from cv2 import cv2
import numpy as np
ImageNumber = 82

#change the following three lines for testing
image = cv2.imread(f".\\{ImageNumber}.jpg", cv2.IMREAD_UNCHANGED ) #path to rgb image
depthimg = np.array(cv2.imread(f".\\d{ImageNumber}.png", cv2.IMREAD_UNCHANGED )) #path to depth image
label_txt = "82.txt" # path to labeled txt

#depthimg = cv2.medianBlur(depthimg,5)
print("Image Reolution: ", image.shape[0], " ", image.shape[1]," ", image.shape[2])
print("Depth Reolution: ", depthimg.shape)

def get_pix(shape, li):
    xw = shape[1]
    yh = shape[0]
    x_cen = int(li[1]* xw)
    y_cen = int(li[2]* yh)
    return [x_cen, y_cen]
    
f=open(label_txt, "r")
l = f.readlines()
red_list = []
blue_list = []
for line in l:
    t = line.split(" ")
    t[4] = t[4].strip("\n")
    tp = [float(a) for a in t]
    if tp[0] == 0.0:
        red_list.append(tp)
    elif tp[0] == 1.0:
        blue_list.append(tp)
f.close()

def draw_dist(l):
    for i in l:
        coord = get_pix(depthimg.shape, i)
        cv2.putText(image,f'{depthimg[coord[1]][coord[0]]/10}cm', (coord[0],coord[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 1)
        cv2.circle(image, (coord[0],coord[1]), radius=1, color=(0,0,255), thickness=-1)
        
        print(f"blue cone center coord is: {coord}")
        print("printing depthimg[coord[1]-5:coord[1]+5,coord[0]-5:coord[0]+5]: ")
        print(depthimg[coord[1]-5:coord[1]+5,coord[0]-5:coord[0]+5])
draw_dist(red_list)
#draw_dist(blue_list)


while True:
    cv2.imshow("image",image)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        cv2.destroyAllWindows()
        break
