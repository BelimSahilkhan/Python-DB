from tkinter import *
from tkinter import ttk

def add_value():
    value = entry.get()

   

    
    tree.insert("", END, values=(value,))

    
    with open("data.txt", "a") as f:
        f.write(value + "\n")

    entry.delete(0, END)   

root = Tk()
root.geometry("400x300")


Label(root, text="Value Enter Kare:").pack()
entry = Entry(root, width=30)
entry.pack(pady=5)

Button(root, text="Add", command=add_value).pack(pady=10)

tree = ttk.Treeview(root, columns=("col1"), show="headings")
tree.heading("col1", text="Entered Value")
tree.pack(expand=True, fill=BOTH)

root.mainloop()
