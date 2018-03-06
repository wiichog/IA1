from tkinter.filedialog import askopenfilename
from PIL import Image
from images import imageAnalizer,getInitial,saveImage,getGoal
from solutions import graph_search
import fw

filename = askopenfilename()
im = Image.open(filename).convert('RGB')
numberOfGroups = int(input("Ingresar numero de grupos para discretizar \n"))
newMatrix = imageAnalizer(im,numberOfGroups)
[[ newMatrix[x][y].setPosition(x,y) for x in range(0,len(newMatrix[y]))] for y in range(0,len(newMatrix))]

numberOfProblem = int(input("Que tipo de problema desea? 1,2,3,4 \n"))
if(numberOfProblem==1):
    fw = fw.frameWork(newMatrix,getInitial(newMatrix),getGoal(newMatrix),1)
elif(numberOfProblem==2):
    fw = fw.frameWork(newMatrix,getInitial(newMatrix),getGoal(newMatrix),2)
elif(numberOfProblem==3):
    fw = fw.frameWork(newMatrix,getInitial(newMatrix),getGoal(newMatrix),3)
elif(numberOfProblem==4):
    fw = fw.frameWork(newMatrix,getInitial(newMatrix),getGoal(newMatrix),4)

saveImage(newMatrix,graph_search(fw))

