import customtkinter
import re, os, logs
from pytube import YouTube
import moviepy.editor as mp
from tkinter import filedialog
from tkinter import *
import tkinter as tk

#https://www.youtube.com/watch?v=GxldQ9eX2wo


def princ():
    
    customtkinter.set_appearance_mode('System')
    customtkinter.set_default_color_theme('green')

    root = customtkinter.CTk()
    root.geometry('1000x348')
    root.title("TransformerMedia")

    def login():
        root = Tk()
        root.withdraw()

        folder_selected = customtkinter.filedialog.askdirectory()

        saida = entry1.get()
        comb = checkbox.get() # 1- marcado | 0 - desmarcado
        comb2 = checkbox2.get()
        entry1.delete(0, END)
        def faz():

            try:

                #link do video q deseja baixar
                link = saida
                print(link)
                path = folder_selected
                print(f"O diretório de download será esse: [ {path} ]\n")

                try:
                    yt = YouTube(link)


                    if comb == 1 and comb2 == 0:
                        print("Baixando...")
                        logs.baixan()
                        ys = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                        ys.download(path)
                        print("Download completo!")
                        logs.concl()
                     
                    if comb == 0 and comb2 == 1:
                        print("Baixando...")
                        logs.baixan()
                        ys = yt.streams.filter(only_audio=True).first().download(path)
                        print("Download completo!")
                    #convertendo video para mp3
                        print(f"convertendo vídeo do link {link} para mp3 ")
                        for file in os.listdir(path):
                            if re.search('mp4', file):
                                mp4_path = os.path.join(path, file)
                                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                                new_file = mp.AudioFileClip(mp4_path)
                                new_file.write_audiofile(mp3_path)
                                os.remove(mp4_path)
        
                        print('Sucesso!!')
                        logs.concl()
                    if comb == 1 and comb2 == 1:
                        print("Baixando...")
                        logs.baixan()
                        ys = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
                        ys.download(path)
                        print("Download completo!")
                        
                        print(f"convertendo vídeo do link {link} para mp3 ")
                        for file in os.listdir(path):
                            if re.search('mp4', file):
                                mp4_path = os.path.join(path, file)
                                mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                                new_file = mp.AudioFileClip(mp4_path)
                                new_file.write_audiofile(mp3_path)
                        
                        print('Sucesso!!')
                        logs.concl()
                    
                    if comb == 0 and comb2 == 0:
                        logs.erro()
                        princ()

                    if root.destroy():
                        print('oi')

                except Exception as erro:
                    print(f'Erro: {erro}')
                    logs.erro()

            except Exception as error:
                print(error)
                logs.erro()
        
        faz()


    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=40, padx=60, fill='both', expand=True)


    label = customtkinter.CTkLabel(master=frame, text='Transformer MP3')
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text='Link', width=800)
    entry1.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text='MP4 (vídeo)')
    checkbox.pack(pady=12, padx=10)

    checkbox2 = customtkinter.CTkCheckBox(master=frame, text='MP3 (audio)')
    checkbox2.pack(padx=0)

    button = customtkinter.CTkButton(master=frame, text='Baixar', command=login)
    button.pack(pady=30, padx=20)

    def fechar():
        root.destroy()
        exit()

    root.protocol('WM_DELETE_WINDOW', fechar)
    root.mainloop()
    
princ()