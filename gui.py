# -*- coding: utf-8 -*-

# UI Library - https://docs.python.org/3/library/tkinter.html
from tkinter import Tk
from tkinter.ttk import Frame, Label, Button
from tkinter.filedialog import askopenfile

# Image Processing Library - https://pillow.readthedocs.io/en/stable/
from PIL import Image, ImageTk

class GUI():
    def __init__(self,
                 processing,
                 window_size:tuple=(500,500),
                 window_name:str='Advanced Tumor Detection Software'):
        '''
        Creating a UI for choose and show image fileCreating a UI for choosing and showing image file.
        
            Parameters:
                processing: function
                    AI processor function
                window_size: tuple, Optional
                    Size of the window(default 500x500)
                window_name: str, Optional
                    Name of the window(default Advanced Tumor Detection Software)
        '''
        self.processing = processing
        
        self.window_size = window_size
        self.window = Tk()
        self.window.title(window_name)
        self.window.geometry(f'{window_size[0]}x{window_size[1]}')
        
        self.__window_config__()
        
        self.window.mainloop()

    def __window_config__(self):
        self.image_frame = Frame(self.window)
        
        Label(self.image_frame, text='Choosen Image')
        self.image_frame.grid(row=1, column=1)
        
        self.window.rowconfigure(2,weight=0)
        self.window.rowconfigure(3,weight=0)
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=1)
        self.window.columnconfigure(2,weight=1)
        
        choose_file = Button(self.window,
                             text='Choose Image',
                             command=self.print_result)

        choose_file.grid(row=3,column=1)
        
        
    def image_processing(self,path:str)->str:
        return self.processing(img_path=path)
        
        
    def open_file(self):
        try:
            self.image_label.image = None
        except:pass
        
        file_types:list = [('Image Files',  ('.png', '.jpg',  '.jpeg',  '.jfif'))]
        
        return askopenfile(mode='r', filetypes=file_types)
        
    
    def read_file(self):
        file_path = self.open_file()
        
        if file_path is None:
            return
            
        file_path_name = file_path.name
        
        image:Image = Image.open(file_path_name)
        
        size:int = int(self.window_size[0]/4)
        
        image_size:tuple = tuple([size,size])
        
        resized = image.resize(image_size)
        
        imageTk = ImageTk.PhotoImage(resized)
        
        self.image_label = Label(self.image_frame, image=imageTk)
        
        self.image_label.image = imageTk
        
        self.image_label.pack()
        
        return file_path_name
        

    def print_result(self):
        img_path = self.read_file()
        
        results,timer = self.image_processing(img_path)
        
        max_key = max(results, key=results.get)
        
        Label(self.window, text=f"{max_key} : {results[max_key]}", foreground='green',font=('Arial',18)).grid(row=1,column=0, columnspan=1,pady=2)
        