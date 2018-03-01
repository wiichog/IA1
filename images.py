import scipy.misc
import statistics
import numpy as np 
from PIL import Image
from node import node

def imageAnalizer(image,number):
    width, height = image.size
    newX = 0
    newY = 0
    xMatrix = []
    yMatrix = []
    for x in range(0,width,number):
        newX += number 
        for y in range(0,height,number):
            newY+= number 
            if(discretizeImage(image.crop((x,y,newX,newY)))==(255,0,0)):
                xMatrix.append(node(discretizeImage(image.crop((x,y,newX,newY))),False,True))
                #xMatrix.append(discretizeImage(image.crop((x,y,newX,newY))))
            else:
                xMatrix.append(node(discretizeImage(image.crop((x,y,newX,newY))),False,False))
                #xMatrix.append(discretizeImage(image.crop((x,y,newX,newY)))) #if you want to see the discretized image descomment line 18 and 22
        yMatrix.append(xMatrix[:])
        xMatrix.clear()
        newY = 0
    #newImage = scipy.misc.imsave('outfile.png', np.asarray(yMatrix))
    return yMatrix

def discretizeImage(image):
    try:
        return classifier(list(statistics.mode(list(image.getdata()))))
    except ValueError:
        return color(list(image.getdata()))

def color(list):
    r = round(statistics.mean([list[i][0] for i in range(len(list))]))
    g = round(statistics.mean([list[i][1] for i in range(len(list))]))
    b = round(statistics.mean([list[i][2] for i in range(len(list))]))
    return classifier((r,g,b))

def classifier(pixel):
    r,g,b = pixel
    if((r==g and r==b and g==b) and (r<100 and g<100 and b<100)):
        return (0,0,0)
    elif((r==g and r==b and g==b) and (r>100 and g>100 and b>100)):
        return (255,255,255)
    elif(statistics.mean((r,g,b))>200):
        return (255,255,255)
    elif(statistics.mean((r,g,b))<10):
        return (0,0,0)
    else:
        if(r>g and r>b):
            return (255,0,0)
        elif(g>r and g>b):
            return (0,255,0)
        else:
            return (r,g,b)


def getInitial(matrix):
    for nodeList in matrix:
        for node in nodeList:
            if(node.initial):                
                return node


