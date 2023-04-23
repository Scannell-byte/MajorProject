import cv2 as cv
import numpy as np
import csv
import glob
import Oat
import Images
import os
from pathlib import Path
import pandas as pd
import math

def appendLists(path,type):
        imageIndex = 1
        count = 0
        for x in os.listdir(path):
            name,extention = os.path.splitext(x)
            if os.path.isfile(os.path.join(path,x)) and  extention == ".tif":
                count += 1
    
        path = os.path.join(path,"*.tif")
        images = [cv.imread(file) for file in glob.glob(path)]
        oats = []

        for i in range(count):
            image = images[i]
            if image is not None:
                mask = cv.cvtColor(image,cv.COLOR_BGR2GRAY) 
                ret, mask = cv.threshold(mask,0,256,cv.THRESH_OTSU)
                oats.append(Images.Image(image,mask))
    
        for image in oats:
            contours,hierarchy = cv.findContours(image.imMask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
            for i in contours:
                print("processing image",imageIndex)
                oat=i
                area = cv.contourArea(oat)
                perimeter = cv.arcLength(oat,True)            
                if (area > 250) and (area < 8000):
                    mask = np.zeros_like(image.image)    
                    imageHSV = cv.cvtColor(image.image,cv.COLOR_BGR2HSV)
                    cv.drawContours(mask,oat,0,(255,255,255),-1)
                    roiBGR = cv.bitwise_and(image.image,mask)
                    indices = np.where(mask == 255)
                    intensePixels = roiBGR[indices]
                    masked_array = np.ma.masked_array(intensePixels, mask=intensePixels==0)
                    masked_array = masked_array.reshape(-1, 3)
                    averageBGR = np.mean(masked_array,axis=(0))
                    averageB = averageBGR[0]
                    averageG = averageBGR[1]
                    averageR = averageBGR[2]
                    
                    roiHSV = cv.bitwise_and(imageHSV,mask)
                    indices = np.where(mask == 255)
                    intensePixels = roiHSV[indices]
                    masked_array = np.ma.masked_array(intensePixels, mask=intensePixels==0)
                    masked_array = masked_array.reshape(-1, 3)
                    averageHSV = np.mean(masked_array,axis=0)
                    averageH = averageHSV[0] * 2 / 3.6
                    averageS = averageHSV[1]
                    averageV = averageHSV[2]
                    moment=(cv.moments(oat, 1))
                    huMoment = (cv.HuMoments(moment))
                    for i in range(0,7):
                        huMoment[i] = (-1* math.copysign(1.0, huMoment[i]) * math.log10(abs(huMoment[i])))
                    #cv.drawContours(image,i,-1,(0,0,255),3)
                    #oats.append(Oat.Oat("Broken",moment,area,perimeter))
                    moment01List.append(huMoment[0])
                    moment02List.append(huMoment[1])
                    moment03List.append(huMoment[2])
                    moment04List.append(huMoment[3])
                    moment05List.append(huMoment[4])
                    moment06List.append(huMoment[5])
                    moment07List.append(huMoment[6])
                    areaList.append(area)
                    perimeterList.append(perimeter)
                    rList.append(averageR)
                    gList.append(averageG)
                    bList.append(averageB)
                    hList.append(averageH)
                    sList.append(averageS)
                    vList.append(averageV)
                    typeList.append(type)
            imageIndex+=1

if __name__ == '__main__':
    cv.namedWindow("Display Window", cv.WINDOW_NORMAL)
    typeList = []

    moment01List = []
    moment02List = []
    moment03List = []
    moment04List = []
    moment05List = []
    moment06List = []
    moment07List = []

    areaList = []
    perimeterList = []
    rList = []
    gList = []
    bList = []
    hList = []
    sList = []
    vList = []
    pathBroken = ("images/scans of different fractions/Broken/")
    pathGroat = ("images/scans of different fractions/groat/")
    pathWholeGrain = ("images/scans of different fractions/wholegrain/")
    appendLists(pathBroken,"Broken")
    appendLists(pathGroat,"groat")
    appendLists(pathWholeGrain,"wholegrain")
    #momentArr = np.array(momentList)
    areaArr = np.array(areaList)
    perimeterArr = np.array(perimeterList)
    typerArr = np.array(typeList)

    data = {
        'type': typerArr,
        'Moment_01': moment01List,
        'Moment_02': moment02List,
        'Moment_03': moment03List,
        'Moment_04': moment04List,
        'Moment_05': moment05List,
        'Moment_06': moment06List,
        'Moment_07': moment07List,

        'Area': areaArr,
        'Perimeter': perimeterArr,
        'Red': rList,
        'Green': gList,
        'Blue': bList,
        'Hue' : hList,
        'Saturation' : sList,
        'Value' : vList}
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    df.to_csv('oatTest.csv', index=False)
    

        
