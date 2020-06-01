# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog, RIGHT, messagebox
from PIL import ImageTk, Image
import miner

dates=zoomfile=classfile=""

LARGE_FONT=("Times","15","bold")
SMALL_FONT=("Verdana","10","bold")

class Control(tk.Tk):
    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        frame = Start(container, self)
        self.frames[Start] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Start)
        self.resizable(False, False)
        self.iconbitmap('icon.ico')

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.config(background='black')
        frame.tkraise()
        
    def close_window(self):
        self.destroy()
        
        
class Start(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        load = Image.open("logo.png")
        render = ImageTk.PhotoImage(load)
        
        img = tk.Label(self, image=render, bg="black")
        img.image = render
        img.place(x=85,y=5)
        img.pack()
        
        label = tk.Label(self, text="Hello professor,",bg="black", fg="white", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        csvLabel = tk.Label(self ,text = "Enter Lecture Date:",  bg="black", fg="white", font=SMALL_FONT)
        csvLabel.pack(pady=10,padx=10)
        dates = tk.Entry(self, width=50)
        dates.pack()
        
        zoom_chat = tk.Button(self, text='Select the Chat text file',font=SMALL_FONT,  width=25, command = lambda : self.uploadz(controller)) 
        zoom_chat.pack(pady=10,padx=10)
        
        class_list = tk.Button(self, text='Select the Class spreadsheet', font=SMALL_FONT,  width=25, command = lambda : self.uploadc(controller)) 
        class_list.pack()

        done_button = tk.Button(self, text="Done",font=LARGE_FONT, command=lambda: self.startexe(dates.get(),controller))
        done_button.pack(side=RIGHT,padx=5, pady=5)
        
    def uploadz(self, controller):
        global zoomfile
        filety= [("text files", "*.txt")]
        zoomfile = filedialog.askopenfilename(parent=self,title='Chat file',filetypes=filety)
        if zoomfile != "":
            tk.messagebox.showinfo(title="Success", message="Well done! Now choose a class list.")
        else:
            tk.messagebox.showerror(title="Error", message="File not chosen. Try again.")
        
    
    def uploadc(self, controller):
        global classfile
        filety= [("excel files", "*.xlsx")]
        classfile = filedialog.askopenfilename(parent=self,title='Class List',filetypes=filety)
        if classfile != "":
            tk.messagebox.showinfo(title="Success", message="Well done! Now click Done.")
        else:
            tk.messagebox.showerror(title="Error", message="File not chosen. Try again.")
        
        
    def startexe(self, dates, controller):
        if dates == "":
            tk.messagebox.showerror(title="Error", message="Please enter the lecture date or description.")
        else:
            try:
                miner.main(dates, zoomfile, classfile)
            except:
                tk.messagebox.showerror(title="Error", message="Wrong table structure! Read Markdown file for assistance.")
            if messagebox.askyesno("Done","Thank you. Do you want to close this app?"):
                controller.close_window()
            else:
                controller.show_frame(Start)
            
        
app = Control()
app.title('Attendance App') 
app.geometry("500x320+300+300")
app.configure(bg='black')
app.mainloop()
        