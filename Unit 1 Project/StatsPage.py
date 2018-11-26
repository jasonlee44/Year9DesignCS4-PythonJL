import tkinter as tk

root = tk.Tk()

output = tk.Text(root,bg="blue", height=10, width=50)
output.config(state="disable")
output.grid(row=0 ,column=0, columnspan=2)

btn1 = tk.Button(root, text="Stat 1")
btn1.grid(row=1, column=0,stick="NESW")

btn2 = tk.Button(root, text="Stat 2")
btn2.grid(row=2, column=0,stick="NESW")

btn3 = tk.Button(root, text="Stat 3")
btn3.grid(row=3, column=0,stick="NESW")







root.mainloop()