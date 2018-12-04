import tkinter as tk
from PIL import ImageTk, Image

username = ""
password = ""
outputStr = ""

def submit():
	print("Submit Pressed")
	username = entryUN.get()
	password = entryPW.get()

	outputStr = "Username: "+username+"\nPassword: "+password
	print(outputStr)



root = tk.Tk()
root.title("Login")
root.geometry("600x600")


labUN = tk.Label(root, text="Username")
labUN.grid(row=0 ,column=1, columnspan=1)

entryUN = tk.Entry(root,bg="#F7F6F6",foreground="black")
entryUN.grid(row=1,column=1,columnspan=1)

labPass = tk.Label(root, text="Password")
labPass.grid(row=2,column=1,columnspan=1)

entryPW = tk.Entry(root,bg="#F7F6F6",foreground="black",show = "*")
entryPW.grid(row=3,column=1,columnspan=1)


btn1 = tk.Button(root, text="Login",command = submit, width=10)
btn1.grid(row=5,column=1,columnspan=1,sticky="S")

loginSelect = tk.Checkbutton()

root.mainloop()









