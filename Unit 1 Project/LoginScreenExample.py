#This imports the tkinter "tool box" this contains
#all the support material t make GUI elements.
#by including "as tk" we are giving a short name to use
import tkinter as tk
from PIL import ImageTk, Image

#With the login page all elements are vertically aligned
#So I am just going to use pack

#Main Window
root = tk.Tk() #creates the standard main window
#Tk() is a special function called CONSTRUCTOR
#If a function is written with a capital letter
#it indicates it is a constructor
labUN = tk.Label(root, text="Username")
labUN.pack()

entUN = tk.Entry(root)
entUN.pack(padx = 10)

labPassword = tk.Label(root,text="Password")
labPassword.pack()

entPassword = tk.Entry(root,show="*")
entPassword.pack()


btnSubmit = tk.Button(root,text="Login")
btnSubmit.pack()

path = "music.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image = img)
panel.thumbnail(50,50)
panel.pack()


#We are writing an EVENT DRIVE PROGRAM.
#Build the GUI
#Wait for "EVENT"
root.mainloop() #Starts the program