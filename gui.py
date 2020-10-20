from imageai.Detection import ObjectDetection
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
import os
import time
import random

num=str(int(random.random()*10))

output_file_name="output\image"+num+".jpg"
execution_path = os.getcwd()
filename="input\image.jpg"
path_image=os.path.join(execution_path,filename)

if(os.path.isfile(path_image)):
   file="input\image.jpg" 
else:
    file="input\image.jpeg"

top=Tk()

buttonText=StringVar()
textI=StringVar()   
timeVar=StringVar()
objectId=StringVar()
countValue=StringVar()


top.resizable(width=True, height=True)

image_path=""

def open_image():
    file_name =filedialog.askopenfilename()
    
    img=Image.open(file_name)
    img=img.resize((850,550), Image. ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image=img

    
    image_path=file_name
    print(file_name)
    print(type(file_name))
    return file_name

# Image display code

img=Image.open(file)
img=img.resize((850,550), Image. ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = Label(top, image = img)
panel.image=img
panel.pack(side = "bottom", fill = "both", expand = "yes")



buttonText.set("Choose File ")    

btn1=Button(top,textvariable=buttonText, fg='white',bg='blue',width=20,command=lambda:set(panel))
btn1.pack(pady=20)





# Object dectition code
def obj_det():
    file_name =filedialog.askopenfilename()
    
    img=Image.open(file_name)
    img=img.resize((850,550), Image. ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image=img
    btn1.config(bg='gray')
    btn1.config(state="disabled")

    buttonText.set("Applying")
    
    textI.set("Processing the image. Please wait!")
    top.update()
    start=time.time()
    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=file_name, output_image_path=os.path.join(execution_path ,output_file_name))
    
    # os.path.join(execution_path , file)
    count=0

    for eachObject in detections:
        print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        # to count number of detected objects
        count+=1
        
    countString="Number of detected objects: "+str(count)
    countValue.set(countString)
        
    #Processing timecalculation
    end=time.time()
    diff=end-start
    timeVar.set("Processing time: "+"{:.2f} s".format(diff))
    


# image updating code
def set(panel):
    obj_det()
    btn1.config(bg='blue')
    top.update()
    btn1.config(state="active")
    buttonText.set("Choose File ")   
    top.update()
    
    textI.set("Output Image with detection boxes")
    top.update()
    
    img=Image.open(output_file_name)
    img=img.resize((850,550), Image. ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image=img




lbl3=Label(top,textvariable=textI).pack()
lbll=Label(top,textvariable=countValue).pack(side="right",padx=20)
lb=Label(top,textvariable=timeVar).pack(side="left",padx=20)
top.mainloop()

