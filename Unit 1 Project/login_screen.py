import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Login")
root.geometry("600x600")


labUN = tk.Label(root, text="Username")
labUN.grid(row=0 ,column=5, columnspan=1)

entryUN = tk.Text(root,height=1,width=15)
entryUN.grid(row=1,column=5,columnspan=1)

labPass = tk.Label(root, text="Password")
labPass

btn1 = tk.Button(root, text="Login")
btn1.grid(row=5,column=2,columnspan=1)



root.mainloop()