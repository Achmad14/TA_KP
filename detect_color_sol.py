import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
    
while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    

    # define range of all color that you want to select in HSV
    lower_premium = np.array([48//2,0//0.39125,39//0.39125]) #HSV Max(180.255.255)
    upper_premium = np.array([70//2,100//0.39125,100//0.39125])
    lower_pertamax = np.array([207//2,87//0.39125,23//0.39125])
    upper_pertamax = np.array([225//2,100//0.39125,40//0.39125])
    lower_kerosene = np.array([48//2,0//0.39125,0//0.39125])
    upper_kerosene = np.array([70//2,100//0.39125,38//0.39125])
    lower_Pertalite = np.array([140//2,58//0.39125,12//0.39125])
    upper_Pertalite = np.array([160//2,100//0.39125,25//0.39125])
    lower_PerPlL = np.array([0//2,84//0.39125,30//0.39125])
    upper_PerPlL = np.array([6//2,97//0.39125,45//0.39125])
    lower_PerPlH = np.array([350//2,84//0.39125,30//0.39125])
    upper_PerPlH = np.array([360//2,97//0.39125,45//0.39125])
    lower_Solar = np.array([30//2,29//0.39125,5//0.39125])
    upper_Solar = np.array([72//2,77//0.39125,20//0.39125])
    lower_NoFuel = np.array([50,10,100])
    upper_NoFuel = np.array([130,80,135])

    # Threshold the HSV image to get only selected colors
    mask_premium = cv2.inRange(hsv, lower_premium, upper_premium)
    mask_pertamax = cv2.inRange(hsv, lower_pertamax, upper_pertamax)
    mask_kerosene = cv2.inRange(hsv, lower_kerosene, upper_kerosene)
    mask_Pertalite = cv2.inRange(hsv, lower_Pertalite, upper_Pertalite)
    mask_PerPlL = cv2.inRange(hsv, lower_PerPlL, upper_PerPlL)
    mask_PerPlH = cv2.inRange(hsv, lower_PerPlH, upper_PerPlH)
    mask_Solar = cv2.inRange(hsv, lower_Solar, upper_Solar)
    mask_NoFuel = cv2.inRange(hsv, lower_NoFuel, upper_NoFuel)
    mask = mask_premium + mask_pertamax + mask_kerosene + mask_Pertalite + mask_PerPlL + mask_PerPlH + mask_Solar + mask_NoFuel
                           
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #Create your ROI
    roi = res[170:170+41,272:272+41]
    roin = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    
    #Take and print value of checking point
    point1 = roin[10,10]
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(res,str(point1),(10,20), font, 0.5,(255,255,255))
    h1 = point1[0]
    s1 = point1[1]
    v1 = point1[2]

    #Take Action with your raspi
    if h1>=24 and h1<=35 and s1>=61 and s1<=255 and v1>=105 and v1<=255:
        cv2.putText(res,'Premium',(10,475), font, 1,(255,255,255))
        
    elif h1>=104 and h1<=109 and s1>=222 and s1<=255 and v1>=59 and v1<=84:
        cv2.putText(res,'Pertamax',(10,475), font, 1,(255,255,255))
        
    elif h1>=24 and h1<=35 and s1>=0 and s1<=60 and v1>=0 and v1<=104:
        cv2.putText(res,'Kerosene',(10,475), font, 1,(255,255,255))
        
    elif h1>=70 and h1<=80 and s1>=150 and s1<=255 and v1>=31 and v1<=64:
        cv2.putText(res,'Pertalite',(10,475), font, 1,(255,255,255))

    elif h1>=0 and h1<=3 and s1>=214 and s1<=248 and v1>=77 and v1<=115:
        cv2.putText(res,'Pertamax Plus',(10,475), font, 1,(255,255,255))
        
    elif h1>=175 and h1<=180 and s1>=214 and s1<=248 and v1>=77 and v1<=115:
        cv2.putText(res,'Pertamax Plus',(10,475), font, 1,(255,255,255))
        
    elif h1>=15 and h1<=36 and s1>=74 and s1<=196 and v1>=13 and v1<=51:
        cv2.putText(res,'Solar',(10,475), font, 1,(255,255,255))

    elif h1>=50 and h1<=130 and s1>=10 and s1<=80 and v1>=100 and v1<=135:
        cv2.putText(res,'No Fuel',(10,475), font, 1,(255,255,255))

    else:
        cv2.putText(res,'Feed Stock',(10,475), font, 1,(255,255,255))

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('roi',roi)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
