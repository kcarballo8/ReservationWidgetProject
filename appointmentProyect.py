#Karen Carballo
#Business App Programming
#Appointment Widget
#import modules
from tkinter import *
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import ttk
from tkcalendar import *

#this function closes the widget
def destroyWindow():
    window.destroy()
    success.destroy()

#calendar function creates calendar to schedule appointment
def calendar():
    cal = Toplevel(window)
    cal.configure(background = "black")
    style = ttk.Style(cal)
    style.theme_use('clam')
    cal.title("Appointments")
    cal.iconbitmap('/Users/karen/Desktop/V Semester/Business app programming/Widgets')
    cal.geometry("500x450")

    #looks for image to place in background
    img2 = PhotoImage(file="image1.png")
    label3 = Label(cal,image=img2)
    label3.place(x=0, y=0)
    #sel label displays the information for the customer
    sel = Label(cal, text= f"{username.get()}, select the day you want to book", 
    width=40, height="1", font=("Comic Sans Ms", 13)) 
    sel.grid(row=0, column=0, padx=100, pady= 10)
    #the call variable has the calendar created
    call = Calendar(cal, selectmode="day",year = 2021, day= 4, 
                normalbackground="black", foreground='dark turquoise', 
                headersforeground='DeepPink3', normalforeground='white')
    call.grid(row=4)
    call.config(background = "black")
    

    #the function grab_date is the one that shows the successful booking
    def grab_date():
        global success
        success = Toplevel(window)
        success.title("Booking")
        success.geometry("150x100")
        img4 = PhotoImage(file="image1.png")
        label4 = Label(success,image=img4)
        label4.place(x=0, y=0)
        Label(success, text="Booking Successful for: " + call.get_date(), wraplength=200, font=("Comic Sans Ms",13)).pack()
        Button(success, text="OK",font=("Comic Sans Ms",13), command=destroyWindow).pack()

    bookBtn = Button(call, text= "Book Date",  bg='black',fg = 'DeepPink2', font=("Comic Sans Ms",13),command=grab_date)
    bookBtn.pack(pady=20)

    cal.mainloop()   

#nails function has the options of nails there are 
def nails():
    global login_screen
    login_screen = Toplevel(window)
    login_screen.title("Options")
    login_screen.geometry("500x450")
    img2 = PhotoImage(file="image1.png")
    label3 = Label(login_screen,image=img2)
    label3.place(x=0, y=0)

    select = Label(login_screen, text= f"{username.get()}, select the option you want", 
    width=40, wraplength=200, height="2", font=("Comic Sans Ms", 13))
    select.pack()
    select.grid(row=0, column=100, padx=100, pady= 10)
 
    #add image to button
    acrylic = PhotoImage(file = "acrylics2.png")
    aPhoto = acrylic.subsample(2,2)
    #btnAcrylic calls the calendar function to book appointment
    btnAcrylic = Button(login_screen, image = aPhoto, command = calendar)
    btnAcrylic.grid(row=200, column=100, padx=80, pady=10)
    
    #add image to button
    dip = PhotoImage(file = "dip.png")
    dPhoto = dip.subsample(2,2)
    #btnDip calls the calendar function to book appointment
    btnDip = Button(login_screen, image = dPhoto, command = calendar)
    btnDip.grid(row=400, column=100, padx=80, pady=10)
    #add image to button
    gel = PhotoImage(file = "gel-nails.png")
    gPhoto = gel.subsample(2,2)
    #btnGel calls the calendar function to book appointment
    btnGel = Button(login_screen, image = gPhoto, command = calendar)
    btnGel.grid(row=600, column=100, padx=80, pady=10)

    login_screen.mainloop()

    
def main_account_screen():
    global username
    global window
    global nameInput
    window = Tk()
    window.geometry("500x450")
    window.title("Account Login")
    #set the background picture
    img = PhotoImage(file="image1.png")
    label = Label(window,image=img)
    label.place(x=0, y=0)

    label1 = Label(window, text="Please enter your name:", width="20", 
    height="1", font=("Comic Sans Ms", 13))
    label1.pack()
    label1.grid(row=0, column=100, padx=100, pady= 10)
    #get input from customer
    username = StringVar()
    nameInput = Entry(window, width = 20, textvariable=username,font=("Comic Sans Ms", 12))
    nameInput.grid(row=100, column=100, padx=150, pady = 5)
    #add image to button
    photo = PhotoImage(file = "image.png")
    photoimage = photo.subsample(8,8)
    #button to schedule appointment, it calls the nails function
    btnSchedule = Button(window, image = photoimage, command = nails)
    btnSchedule.grid(row=200, column=100, padx=80, pady=10)

    window.mainloop()
 
 
main_account_screen()

