#By Jason Lee

import tkinter as tk
from PIL import ImageTk, Image

username = ""
password = ""
outputStr = ""
userPass = {}
x=""
text = ""



def loginOption():
	global x
	x=int("1")
	print(x)

def signupOption():
	global x
	x=int("2")
	print(x)


root = tk.Tk()
root.configure(background="#52B3FF")
v = tk.IntVar()
root.title("Login")
root.geometry("300x300")
text=""
def submit():
	global text
	username = entryUN.get()
	password = entryPW.get()
	outputStr = "Username: "+username+"\nPassword: "+password
	print(outputStr)

	if x==1:
		if (username in userPass) == False:		
			outputText.config(state="normal")
			outputText.delete('1.0','end')
			outputText.insert(tk.INSERT,"Wrong username or password")
			outputText.config(state="disabled")
		else:
		    if userPass[username] != password:
		    	outputText.config(state="normal")
		    	outputText.delete('1.0','end')
		    	outputText.insert(tk.INSERT,"Wrong username or password")
		    	outputText.config(state="disabled")
		    else:
		    	outputText.config(state="normal")
		    	outputText.delete('1.0','end')
		    	outputText.insert(tk.INSERT,"Login Successful")
		    	outputText.config(state="disabled")
	if x==2:
		if username in userPass:
			outputText.config(state="normal")
			outputText.delete('1.0','end')
			outputText.insert(tk.INSERT,"Username already exists")
			outputText.config(state="disabled")
		else:
			entryUN.delete('0','end')
			entryPW.delete('0','end')
			outputText.config(state="normal")
			outputText.delete('1.0','end')
			outputText.insert(tk.INSERT,"Please login")
			outputText.config(state="disabled")			
			userPass[username] = password


labUN = tk.Label(root, text="Username",background="#52B3FF")
labUN.grid(row=0 ,column=1, columnspan=1)

entryUN = tk.Entry(root,bg="#F7F6F6",foreground="black")
entryUN.grid(row=1,column=1,columnspan=1)

labPass = tk.Label(root, text="Password",background="#52B3FF")
labPass.grid(row=2,column=1,columnspan=1)

entryPW = tk.Entry(root,bg="#F7F6F6",foreground="black",show = "*")
entryPW.grid(row=3,column=1,columnspan=1)

btn1 = tk.Button(root, text="Submit",command = submit, width=10,background="#52B3FF")
btn1.grid(row=5,column=1,columnspan=1,sticky="S")

#-----Outputs (please login,username already exists)
outputText = tk.Text(root,width=30,height=1)
outputText.grid(row=8, column=1,sticky="W")
outputText.config(state="disabled",bg="#52B3FF",borderwidth=1,highlightthickness=0,foreground="white")

#----Radio buttons to select 'login' or 'sign up'---------
loginSelect = tk.Radiobutton(root,text="Login",variable=v,value=1,background="#52B3FF",command=loginOption)
loginSelect.grid(row=6,column=1,sticky="W")


signupSelect = tk.Radiobutton(root,text="Sign Up",variable=v,value=2,background="#52B3FF",command=signupOption)
signupSelect.grid(row=7,column=1,sticky="W")

root.mainloop()
