from tkinter.filedialog import askopenfilename
from PIL import Image
import fw
import images


filename = askopenfilename()
im = Image.open(filename).convert('RGB')
numberOfGroups = int(input("Ingresar numero de grupos para discretizar \n"))
nodeMatrix = images.imageAnalizer(im,numberOfGroups)