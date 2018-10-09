import tkinter as tk

root = tk.Tk() 	#Tk() is a special method called a constructor 
				#A constructor is a spcial method only called once
				#It sets everything up for us. 


lab = tk.Label(root, text = "Enter a number:")
#To pack a element usign the grid geometry manager. We use
# <object>.grid(<parameters>)

lab.grid(row = 0, column = 0)
lab.configure(bg="brown")x

ent = tk.Entry(root)
ent.grid(row = 1, column = 0)
ent.configure(bg="black")

btn = tk.Button(root, text = "Press Me")
btn.grid(row = 2, column = 0)



output = tk.Text(root)
output.configure(state = "disable", bg = "beige")
output.grid(row = 0, column = 1, rowspan = 3)


root.mainloop()