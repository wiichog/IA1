import scipy.misc
import statistics
import numpy as np 
from PIL import Image

def imageAnalizer(image,number):
    width, height = image.size
    newX = 0
    newY = 0
    xMatrix = []
    yMatrix = []
    x = 0
    y = 0
    for x in range(0,width,number):
        newX += number
        for y in range(0,height,number):
            newY+= number
            newPixel = discretizeImage(image.crop((x,y,newX,newY)))
            xMatrix.append(newPixel)
            y = newY
        yMatrix.append(xMatrix[:])
        xMatrix.clear()
        x = newX
        newY = 0
    newImage = scipy.misc.imsave('outfile.png', np.asarray(yMatrix))
    return image

def discretizeImage(image):
    try:
        return statistics.mode(list(image.getdata()))
    except ValueError:
        return color(list(image.getdata()))

def color(list):
    r = round(statistics.mean([list[i][0] for i in range(len(list))]))
    g = round(statistics.mean([list[i][1] for i in range(len(list))]))
    b = round(statistics.mean([list[i][2] for i in range(len(list))]))
    if((r==g and r==b and g==b) and (r<100 and g<100 and b<100)):
        return (0,0,0)
    elif((r==g and r==b and g==b) and (r>100 and g>100 and b>100)):
        return (255,255,255)
    elif(statistics.mean((r,g,b))>200):
        return (255,255,255)
    else:
        if(r>g and r>b):
            return (255,0,0)
        elif(g>r and g>b):
            return (0,255,0)



