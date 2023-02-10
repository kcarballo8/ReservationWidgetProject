#import modules
from tkinter import *
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import ttk
from tkcalendar import *

def calendar():
    calen = Toplevel(window)
    calen.title("Appointments")
    calen.iconbitmap('/Users/karen/Desktop/V Semester/Business app programming/Widgets')
    calen.geometry("350x220")
    img2 = PhotoImage(file="/Users/karen/Desktop/Widget Project/image1.png")
    label3 = Label(calen,image=img2)
    label3.place(x=0, y=0)

    cal = Calendar(calen, selectmode="day",year = 2021, day= 4)
    cal.pack(pady=5)
    def grab_date():
        mylabel.config(text="Today's Date is " + cal.get_date())
        
    btn = Button(cal, text= "Get Date", command=grab_date)
    btn.pack(pady=20)
    mylabel = Label(cal, text="")
    mylabel.pack(pady=20)
    calen.mainloop()   

def acrylicNails():
    acrylicScreen = Toplevel(window)
    login_screen.geometry("500x450")
    img2 = PhotoImage(file="image1.png")
    label3 = Label(login_screen,image=img2)
    label3.place(x=0, y=0)
    sel = Label(login_screen, text= f"{username.get()}, select the day you want to book", 
    width=40, height="1", font=("Arial Bold", 13))  
    sel.pack()
    sel.grid(row=0, column=100, padx=100, pady= 10)
    calendar()
    acrylicScreen.mainloop()
    

def nails():
    global login_screen
    login_screen = Toplevel(window)
    login_screen.title("Options")
    login_screen.geometry("500x450")
    img2 = PhotoImage(file="image1.png")
    label3 = Label(login_screen,image=img2)
    label3.place(x=0, y=0)

    select = Label(login_screen, text= f"{username.get()}, select the option you want", width=40, height="1", font=("Arial Bold", 13))
    select.pack()
    select.grid(row=0, column=100, padx=100, pady= 10)
 
    acrylic = PhotoImage(file = "acrylics2.png")
    aPhoto = acrylic.subsample(2,2)
    btnAcrylic = Button(login_screen, image = aPhoto, command = calendar)
    btnAcrylic.grid(row=200, column=100, padx=80, pady=10)

    dip = PhotoImage(file = "dip.png")
    dPhoto = dip.subsample(2,2)
    btnAcrylic = Button(login_screen, image = dPhoto)
    btnAcrylic.grid(row=400, column=100, padx=80, pady=10)

    gel = PhotoImage(file = "gel-nails.png")
    gPhoto = gel.subsample(2,2)
    btnAcrylic = Button(login_screen, image = gPhoto)
    btnAcrylic.grid(row=600, column=100, padx=80, pady=10)

    login_screen.mainloop()

    
def nameofPerson():
   
    username_info = username.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.close()
 
    nameInput.delete(0, END)

 
def main_account_screen():
    global username
    global window
    global nameInput
    window = Tk()
    window.geometry("500x450")
    window.title("Account Login")
    img = PhotoImage(file="image1.png")
    label = Label(window,image=img)
    label.place(x=0, y=0)


    label1 = Label(window, text="Please enter your name:", width="20", height="1", font=("Arial Bold", 13))
    label1.pack()
    label1.grid(row=0, column=100, padx=100, pady= 10)

    username = StringVar()
    nameInput = Entry(window, width = 20,  fg="pink", textvariable=username)
    nameInput.grid(row=100, column=100, padx=150, pady = 5)

  

    photo = PhotoImage(file = "image.png")
    photoimage = photo.subsample(8,8)
    btnAdd = Button(window, image = photoimage, command = nails)
    btnAdd.grid(row=200, column=100, padx=80, pady=10)
    window.mainloop()
 
 
main_account_screen()

