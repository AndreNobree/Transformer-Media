import customtkinter
import re, os
from tkinter import *

#https://www.youtube.com/watch?v=nzvwHv2Iq10




def logErr():

    def fechar():
        root1.destroy()

    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('dark-blue')

    root1 = customtkinter.CTk()
    root1.geometry('200x100')
    root1.title("Log")


    frame = customtkinter.CTkFrame(master=root1)
    frame.pack(pady=10, padx=10, fill='both', expand=True)


    label = customtkinter.CTkLabel(master=frame, text='Erro, Reveja os campos')
    label.pack(pady=5, padx=10)

    button = customtkinter.CTkButton(master=frame, text='Fechar', command=fechar)
    button.pack(pady=10, padx=20)

    root1.mainloop()

def logAcert():

    def fechar():
        root1.destroy()

    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('dark-blue')

    root1 = customtkinter.CTk()
    root1.geometry('200x100')
    root1.title("Log")


    frame = customtkinter.CTkFrame(master=root1)
    frame.pack(pady=10, padx=10, fill='both', expand=True)


    label = customtkinter.CTkLabel(master=frame, text='DOWNLOAD CONCLUIDO')
    label.pack(pady=5, padx=10)

    button = customtkinter.CTkButton(master=frame, text='Fechar', command=fechar)
    button.pack(pady=10, padx=20)

    root1.mainloop()

