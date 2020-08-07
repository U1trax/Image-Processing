from tkinter import * 
import cv2 
import matplotlib as mpl mpl.use('TkAgg') 
import numpy as np  from matplotlib.backends.backend_tkagg 
import FigureCanvasTkAgg from matplotlib.figure 
import Figure from tkinter 
import filedialog class high_pass: 
    path = 'D:\Program Files\Projects\College\IPMV\cameraman.tif'     
    def __init__(self, master): 
    self.frame1 = Frame(master)         
    self.frame2 = Frame(master)         
    self.frame3 = Frame(master)         
    hbtn = Button(self.frame2, text="OPEN IMAGE", command=lambda: self.button_click(master))         
    hbtn.pack(fill="none", expand=True)         
    self.initUI(master)     
    def initUI(self, master): 
    self.frame1.grid(row=0, column=0)         
    self.frame2.grid(row=10, column=0)         
    if len(high_pass.path) > 0: 
