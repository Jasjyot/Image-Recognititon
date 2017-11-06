import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
from statistics import mean
from collections import Counter

def createExamples():
    numberArrayExamples=open('numArEx.txt','a')
    numbersWeHave=range(0,10)
    versionsWeHave=range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
            print(str(eachNum)+'.'+str(eachVer))
            imageFilePath='images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
            ei=Image.open(imageFilePath)
            eiar=np.array(ei)
            eiar1=str(eiar.tolist())
            numberArrayExamples.write(str(eachNum)+"::"+eiar1+'\n')

def whatNumIsThis(filePath):
    matchedAr=[]
    loadExamps=open('numArEx.txt','r').read()
    loadExamps=loadExamps.split('\n')

    i=Image.open(filePath)
    iar=np.array(i)
    iarl=iar.tolist()

    inQuestion=str(iarl)

    for eachExample in loadExamps:
        if len(eachExample)>2:
            splitEx= eachExample.split('::')
            currentNum=splitEx[0]
            currentAr=splitEx[1]

            eachPixEx=currentAr.split('],')
            eachPixInQ=inQuestion.split('],')

            x=0
            while(x<len(eachPixEx)):
                if eachPixEx[x]==eachPixInQ[x]:
                    matchedAr.append(int(currentNum))
                x+=1
    
    print(matchedAr)
    x=Counter(matchedAr)
    print(x)

    graphX=[]
    graphY=[]

    for eachThing in x:
        graphX.append(eachThing)
        graphY.append(x[eachThing])
    
    fig=plt.figure()
    ax1=plt.subplot2grid((4,4),(0,0),rowspan=1, colspan =4)
    ax2=plt.subplot2grid((4,4),(1,0),rowspan=3, colspan =4)

    ax1.imshow(iar)
    ax2.bar(graphX, graphY, align='center')
    plt.ylim(400)
    plt.show()





def threshold(imageArray):
    balanceAr=[]
    newAr=imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            print (eachPix)
            #time.sleep(5)

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = mean(eachPix[:3])
            balanceAr.append(avgNum)
    
    balance=mean(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if mean(eachPix[:3])>balance:
                eachPix[0]=255
                eachPix[1]=255
                eachPix[2]=255
                eachPix[3]=255

            else:
                eachPix[0]=0
                eachPix[1]=0
                eachPix[2]=0
                eachPix[3]=255


#createExamples()

whatNumIsThis('6.2.png')




















'''
    for eachRow in newAr:
        for eachPix in eachRow:
            print (eachPix)
    
i1=Image.open('/Users/jasjyotsingh/Documents/Python/Image_Recognition/images/numbers/y0.3.png')
iarr1=np.array(i1)


i2=Image.open('/Users/jasjyotsingh/Documents/Python/Image_Recognition/images/numbers/y0.4.png')
iarr2=np.array(i2)


i3=Image.open('/Users/jasjyotsingh/Documents/Python/Image_Recognition/images/numbers/y0.5.png')
iarr3=np.array(i3)


i4=Image.open('/Users/jasjyotsingh/Documents/Python/Image_Recognition/images/sentdex.png')
iarr4=np.array(i4)

threshold(iarr1)
threshold(iarr2)
threshold(iarr3)
threshold(iarr4)


ax1 = plt.subplot2grid((8,6),(0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6),(4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6),(0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6),(4,3), rowspan=4, colspan=3)

ax1.imshow(iarr1)
ax2.imshow(iarr2)
ax3.imshow(iarr3)
ax4.imshow(iarr4)


plt.show()
'''