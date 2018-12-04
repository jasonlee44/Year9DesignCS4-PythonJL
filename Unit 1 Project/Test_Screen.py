import tkinter as tk

def change(*args):
	print(var.get())

root = tk.Tk()
root.title("Music")
root.geometry("400x250")

x = tk.Label(root,text="")
x.grid(row=2, column=0)

questionText = tk.Label(root,text="Question")
questionText.grid(row=3, column=0, sticky ="W")

question = tk.Entry(root)
question.config(state="disable")
question.grid(row=4, column=0, columnspan=1)

hint = tk.Checkbutton(root,text="Hint")
hint.grid(row=5,column=0,sticky="W")

answerText = tk.Label(root,text="Answer")
answerText.grid(row=3, column=1,sticky="W")

answer = tk.Entry(root)
answer.grid(row=4, column=1, columnspan=1)

submit = tk.Button(root, text="Submit")
submit.grid(row=5,column=1)

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


root.mainloop()
print("End program")