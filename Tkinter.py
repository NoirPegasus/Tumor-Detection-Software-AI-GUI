import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import time
from tensorflow import keras
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
import numpy as np

ws = Tk()
ws.title('Advanced Tumor Detection Software')
ws.geometry('625x500')


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpg')])
    if file_path is not None:
        global file_path3
        file_path1= file_path.name
        file_path3 = file_path.name
        print(file_path1)
        frame1 = Frame(ws)
        Label(frame1,text="alkmwdlkawdm")
        frame1.grid(row=1,column=1)
        im = Image.open(file_path1)
        limg = im.resize((100, 100))
        img = ImageTk.PhotoImage(limg)
        imgla = Label(frame1, image=img)
        imgla.image = img
        imgla.pack()
        scan()
        ##imgla.grid(row=1, column=1,columnspan=1, rowspan=2,pady=50)


##img = PhotoImage(file= r'C:\Users\CP\Desktop\berkaytubitak\logo.png')
##img1 = img.subsample(3, 3)
##Label(ws, image=img1).grid(row=0, column=1,
                                 ##  columnspan=1, rowspan=2, padx=5, pady=5

def scan():
    model = keras.models.load_model("brain-tumor.h5")
    index = ['glioma', 'meningioma', 'normal', 'adenoma']

    test_image2 = load_img(file_path3, target_size=(224, 224))
    test_image2

    test_image2 = img_to_array(test_image2)
    test_image2 = np.expand_dims(test_image2, axis=0)
    result2 = np.argmax(model.predict(test_image2 / 255.0), axis=1)
    print(index[result2[0]])
    global response
    response = index[result2[0]]



def uploadFiles():
    for i in range(5):
        pb1.grid(row=5, columnspan=3)
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text=response, foreground='green',font=('Arial',18)).grid(row=1,column=0, columnspan=1, pady=20)
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=5, columnspan=3, pady=20)




adhar = Label(
    ws,
    text='Upload Target File',
    font=('Arial',10)

)
adhar.grid(row=2, column=1)
ws.rowconfigure(2,weight=0)
ws.rowconfigure(3,weight=0)
ws.columnconfigure(0,weight=1)
ws.columnconfigure(1,weight=1)
ws.columnconfigure(2,weight=1)


adharbtn = Button(
    ws,
    text='Choose File',
    command=lambda: open_file()
)
adharbtn.grid(row=3, column=1)



upld = Button(
    ws,
    text='Upload Files',
    command=uploadFiles,

)
upld.grid(row=4, columnspan=3, pady=20)

pb1 = Progressbar(
        ws,
        length=300,
        mode='determinate'
    )
pb1.grid(row=5, columnspan=3, pady=20)
ws.mainloop()