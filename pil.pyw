import PIL
from PIL import Image
import os, glob, sys
import Tkinter, Tkconstants, tkFileDialog
import tkMessageBox
basewidth = 800
import Tkinter as tk
from Tkinter import BOTTOM, TOP, BOTH, YES
import ttk
import subprocess


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="Convertir", command=self.start)
        self.salir = ttk.Button(text="Salir", command=quit)
        self.button.pack(side = TOP, fill = BOTH, expand = YES)
        
        self.progress = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(side = BOTTOM, fill = BOTH)
        self.salir.pack(side = BOTTOM)
        self.bytes = 0
        self.maxbytes = 0

    def start(self):
        app.directory = tkFileDialog.askdirectory()
        self.lista = glob.glob(app.directory+"/*.jpg")
        self.progress["value"] = 0
        if len(self.lista) != 0:
            self.maxbytes = len(self.lista)
            self.progress["maximum"] = len(self.lista)
            self.read_bytes()
        else:
            tkMessageBox.showinfo("Mensaje", "La carpeta seleccionada no tiene imagenes jpg")

    def read_bytes(self):
        self.bytes += 1
        self.progress["value"] = self.bytes
        img = Image.open(self.lista[self.bytes-1])
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.save(app.directory+"/"+str(self.bytes-1)+'.jpg')
        if self.bytes < self.maxbytes:
            self.after(10, self.read_bytes)
        if self.progress["value"] == len(self.lista):
            tkMessageBox.showinfo("Mensaje", "Conversion terminada!")
            self.progress["value"] = 0
            subprocess.Popen(r'explorer '+"\""+app.directory.replace('/','\\')+"\\\"")
            self.lista = []
            self.progress["value"] = 0
            self.bytes = 0
        

app = SampleApp()
app.title( "PSC Redimensionador" )
app.geometry( "250x150" )
app.mainloop()
