from tkinter.filedialog import askopenfilename
from PIL import Image
import fw
import images


filename = askopenfilename()
im = Image.open(filename).convert('RGB')
images.imageAnalizer(im,20)