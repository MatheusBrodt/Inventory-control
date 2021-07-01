from tkinter import *
from tkinter import ttk

tela = Tk()


class FullScreen:
    def __init__(self):
        self.tela = tela
        tela.mainloop()


    def features(self):
        self.tela.title('Laboratório Carol')
        self.tela.geometry('1360x720')
        self.tela.resizable()
        self.tela.minsize()
        self.tela.configure()

FullScreen()
