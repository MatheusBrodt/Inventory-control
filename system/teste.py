from tkinter import *
from tkinter import ttk
import mysql.connector

login = Tk()

class Interface_Login():
    def __init__(self):
        self.login = login
        self.tela_login()
        self.user()
        login.mainloop()

    def tela_login(self):
        self.login.title('Login Usuário')
        self.login.geometry('300x200')
        self.login.resizable(False, False)
        self.login.configure(background='Blue')

    def user(self):
        self.userLogin = Label(self.login, text='Usuário', bg='white', fg='black')
        self.userLogin.place(relx=0.04, rely=0.10, relwidth=0.25, relheight=0.42)


Interface_Login()