import cv2 as cv
import numpy as np
import csv

if __name__ == '__main__':
    cv.namedWindow("Display Window", cv.WINDOW_NORMAL)
    image = cv.imread("images\scans of different fractions\Broken\BrokenTest.tif")
    
    imMask = cv.cvtColor(image,cv.COLOR_BGR2GRAY) 
    ret, imMask = cv.threshold(imMask,0,256,cv.THRESH_OTSU)
    contours,hierarchy = cv.findContours(imMask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    moment = []
    cnt = []
    for i in contours:
        
        area = cv.contourArea(i)
        if (8000 > area > 250):# and (area < 8000):
            cnt.append(i)
            moment.append(cv.moments(i))
            mask = np.zeros_like(image)    
            imageHSV = cv.cvtColor(image,cv.COLOR_BGR2HSV)
            cv.drawContours(mask,i,0,(255,255,255),-1)
            roiBGR = cv.bitwise_and(image,mask)
            indices = np.where(mask == 255)
            intensePixels = roiBGR[indices]
            masked_array = np.ma.masked_array(intensePixels, mask=intensePixels==0)
            masked_array = masked_array.reshape(-1, 3)
            averageBGR = np.mean(masked_array,axis=(0))
            print(averageBGR)
            print(averageBGR[0])
            print(averageBGR[1])
            print(averageBGR[2])
            
            roiHSV = cv.bitwise_and(imageHSV,mask)
            indices = np.where(mask == 255)
            intensePixels = roiHSV[indices]
            masked_array = np.ma.masked_array(intensePixels, mask=intensePixels==0)
            masked_array = masked_array.reshape(-1, 3)
            averageHSV = np.mean(masked_array,axis=0)
            averageH = averageHSV[0] * 2 / 3.6
            print(averageHSV)
            print(averageH)
            print(averageHSV[1])
            print(averageHSV[2])
    cv.imshow("Display Window",imageHSV)
            #currentCnt = cv.bitwise_and(image,mask)
            #currentCntRGB = cv.cvtColor(currentCnt,cv.COLOR_BGR2RGB)
            #averageRGB = np.mean(currentCntRGB, axis = (0,1))
            #print(averageRGB)
    
    

    # file = open("oatTest.csv","w")
    # writer = csv.writer(file)
    # count = 0

    # for i in moment:
    
    #     header =[]
    #     data = []

    #     if count == 0:

    #         for x in i:
    #             header.append(x)
    #         count = 1
    #         writer.writerow(header)
                
    #     for x in i:
    #         data.append(i[x])
    #     writer.writerow(data)
        
    k = cv.waitKey(0)