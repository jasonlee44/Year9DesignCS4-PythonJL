#By Jason Lee

import tkinter as tk
from PIL import ImageTk, Image
import random

#—––Opens and reads the file with the questions and answers———
file=open("File.txt","r")
tempd=file.read()
list1=tempd.split("\n")
list1.sort()
rand=random.randint(0,len(list1)-1)
QandA=list1[rand]
locstar=QandA.index(":")
solution=[]
solution.append(QandA[0:locstar])
solution.append(QandA[locstar+1:])
print(solution)


#—––––––––––––––––––––––––––––––––––––––––––
def change(*args):
	print(var.get())

#—––––––––––––––––––––––––––––––––––––––––––
root = tk.Tk()
root.title("Music Test")
root.geometry("700x520")
root.config(bg="#61B4EA")

#—––Checks to see if the answer is correct———
def press():
	answerInput=answer.get()
	print(answerInput)

	if answerInput==solution[1]:
		txt1.config(state="normal")
		txt1.delete('1.0','end')
		txt1.insert(tk.INSERT,"Correct!")
		txt1.config(state="disabled")
		solution.pop(0)
		solution.pop(0)
		rand=random.randint(0,len(list1)-1)
		QandA=list1[rand]
		locstar=QandA.index(":")
		solution.append(QandA[0:locstar])
		solution.append(QandA[locstar+1:])
		question.config(state="normal")
		question.delete('1.0','end')
		question.insert(tk.INSERT,"How many sharps does the key of '"+solution[0]+"' have?")
		question.config(state="disable")
		answer.delete('0','end')
		print(solution)

	else:
		txt1.config(state="normal")
		txt1.delete('1.0','end')
		txt1.insert(tk.INSERT,"Incorrect!")
		txt1.config(state="disabled")

#———When the hint checkbox is clicked, the image will pop up———
def showImg(*args):
	if var2.get()==1:
		panel.config(state="normal")
	if var2.get()==0:
		panel.config(state="disabled")

#———Accessibility, changes the background colour of widgets to white———
def accessibility():
	if var3.get()==1:
		root.config(bg="white")
		questionText.config(bg="white")
		hint.config(bg="white")
		answerText.config(bg="white")
		lb1.config(bg="white")
		panel.config(bg="white",foreground="white")
		txt1.config(bg="white")

	if var3.get()==0:
		root.config(bg="#61B4EA")
		questionText.config(bg="#009AFF")
		hint.config(bg="#61B4EA")	
		answerText.config(bg="#009AFF")	
		lb1.config(bg="#61B4EA")
		panel.config(bg="#61B4EA",foreground="#1E7B00")
		txt1.config(bg="#61B4EA")

#—––––––––––––––––––––––––––––––––––––––––––
questionText = tk.Label(root,text="Question",bg="#009AFF")
questionText.grid(row=3, column=0, sticky ="W")

#———Entry box for the questions———
question = tk.Text(root,width=45,height=1)
question.insert(tk.INSERT,"How many sharps does the key of '"+solution[0]+"' have?")
question.config(state="disable")
question.grid(row=4, column=0,sticky="NSW")

#———Check box for hint———
var2 = tk.IntVar()
hint = tk.Checkbutton(root,text="Hint",variable = var2, command=showImg,bg="#61B4EA")
hint.grid(row=6,column=0,sticky="W")

#—––––––––––––––––––––––––––––––––––––––––––
answerText = tk.Label(root,text="Answer",bg="#009AFF")
answerText.grid(row=3, column=1,sticky="W")

#———Entry box for answer———
answer = tk.Entry(root)
answer.grid(row=4, column=1, columnspan=1)

#—––––––––––––––––––––––––––––––––––––––––––
submit = tk.Button(root, text="Submit",command = press,width=10,bg="#61B4EA")
submit.grid(row=7,column=1,rowspan=1,sticky="N")

#———Drop down menu for the type of questions———
OPTIONS = [
	"Sharp ♯",
	"Flat ♭",
	"Random",
]

var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)

dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1],OPTIONS[2])
dropDownMenu.grid(row=1, column=0, sticky="W")

#—––––––––––––––––––––––––––––––––––––––––––
lb1 = tk.Label(root,bg="#61B4EA")
lb1.grid(row=2,column=0)

#—––––––––––––––––––––––––––––––––––––––––––
img = ImageTk.PhotoImage(Image.open("circle-of-fifths.png"))
panel = tk.Label(root, image = img,bg="#61B4EA")
panel.config(state="disabled")
panel.grid(row=7,column=0)

#—––––––––––––––––––––––––––––––––––––––––––
txt1=tk.Text(root,width=15,height=1)
txt1.grid(row=7,column=2,sticky="NW")
txt1.config(state="disabled",bg="#61B4EA",borderwidth=1,highlightthickness=0,foreground="#1E7B00",font=("Arial",26))

#—––––––––––––––––––––––––––––––––––––––––––
var3=tk.IntVar()
acc=tk.Checkbutton(root,text="Accessibility",variable=var3,command=accessibility)
acc.grid(row=1,column=2,sticky="W")

root.mainloop()
print("End program")
