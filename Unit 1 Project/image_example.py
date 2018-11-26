import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("600x780")
window.configure(background='grey')

path = "100_Fermium.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = img, height = 500,width=200)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack()

#Start the GUI
window.mainloop()