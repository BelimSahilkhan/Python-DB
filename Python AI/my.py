from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from tkinter import ttk

def init():
    con=sq.connect("my1.db")
    cur=con.cursor()
    cur.execute("create table if not exists Product(id integer primary key autoincrement,name text,price integer,category text)")
    cur.close()
    con.close()
init()

root=Tk()

lb=LabelFrame(root,text="Insert Record",height=150,width=450)
lb.pack(fill="x")

lbl1=Label(lb,text="Name")
lbl1.place(x=20,y=20)
e1=Entry(lb)
e1.place(x=80,y=20)

lbl2=Label(lb,text="Price")
lbl2.place(x=20,y=50)
e2=Entry(lb)
e2.place(x=80,y=50)

lbl33 = Label(lb, text="Category") 
lbl33.place(x=20, y=80) 
e33 = Entry(lb) 
e33.place(x=80, y=80)

def Insert_record():
    nm=e1.get()
    pc=e2.get()
    ca=e33.get()
    if(nm=="" or pc==""):
        messagebox.showinfo("Error","Plese Enter Both Field...")
    else:
        con=sq.connect("my1.db")
        cur=con.cursor()
        cur.execute("insert into Product(name,price,category)values(?,?,?)",(nm,pc,ca))
        con.commit()
        cur.close()
        con.close()
        e1.delete(0,END)
        e2.delete(0,END)
        e33.delete(0,END)
        e1.focus()
        messagebox.showinfo("message","Record Inserted...")

btn1=Button(lb,text="Save",command=Insert_record)
btn1.place(x=100,y=100)

lb1=LabelFrame(root,text="Search Record",height=100,width=450)
lb1.pack(fill="x")

lbl3=Label(lb1,text="Name")
lbl3.place(x=20,y=20)
e3=Entry(lb1)
e3.place(x=80,y=20)

def Insert_record():
    nm=e3.get()
    

btn1=Button(lb1,text="Search",command=Insert_record)
btn1.place(x=220,y=17)

lb2=LabelFrame(root,text="View Record",height=200,width=450)
lb2.pack(fill="x")
con=sq.connect("my1.db")
tree = ttk.Treeview(lb2, columns=("id", "name", "price","category"))
tree.heading("id", text="ID")
tree.heading("name", text="Name")
tree.heading("price", text="Price")
tree.heading("category", text="Category")
tree.column("id",width=50,anchor=CENTER)
tree.column("name",width=150,anchor=CENTER)
tree.column("price",width=100,anchor=CENTER)
tree.column("category",width=100,anchor=CENTER)
tree.pack(fill=BOTH, expand=True, padx=10, pady=10)
cur=con.cursor();
cur = con.cursor()
cur.execute("SELECT * FROM Product ORDER BY category")
rows = cur.fetchall()

# --- Dictionary to store category parents ---
categories = {}

for row in rows:
    idd, name, price, category = row
    
    # If category not yet added as parent, add it
    if category not in categories:
        cat_id = tree.insert("", END, text=category, values=("", "", "", category))
        categories[category] = cat_id
    
    # Insert product as child of category
    tree.insert(categories[category], END, values=row)

con.close()

    
def Edit_Record():
    top=Toplevel(root)
    top.title("Edit")
    lb=LabelFrame(top,text="Update Record",height=300,width=450)
    lb.pack(fill="x")

    lbl=Label(lb,text="Id")
    lbl.place(x=20,y=20)
    e=Entry(lb)
    e.place(x=80,y=20)
    lbl1=Label(lb,text="Name")
    lbl1.place(x=20,y=50)
    e1=Entry(lb)
    e1.place(x=80,y=50)

    lbl2=Label(lb,text="Price")
    lbl2.place(x=20,y=80)
    e2=Entry(lb)
    e2.place(x=80,y=80)

    def Editt():
        idd=e.get()
        nm=e1.get()
        pc=e2.get()
        if(idd=="" or nm=="" or pc==""):
            messagebox.showinfo("Error","Plese Fill Up...")
        else:
            con=sq.connect("my1.db")
            cur=con.cursor()
            cur.execute("update stud set name=?,price=? where id=?",(nm,pc,e.get()))
            con.commit()
            cur.close()
            con.close()
            e.delete(0,END)
            e1.delete(0,END)
            e2.delete(0,END)
            e1.focus()
            messagebox.showinfo("message","Record Updatad...")
            top.destroy()

    btn1=Button(lb,text="Edit",command=Editt)
    btn1.place(x=80,y=110)

    top.geometry("500x500")
    top.mainloop()

f1=Frame(root,height=50,width=450)
f1.pack(fill="x")

btn2=Button(f1,text="Edit",command=Edit_Record)
btn2.place(x=20,y=20)

def Delete_Record():
    top=Toplevel(root)
    top.title("Edit")
    lb=LabelFrame(top,text="Delete Record",height=300,width=450)
    lb.pack(fill="x")

    lbl=Label(lb,text="Id")
    lbl.place(x=20,y=20)
    e=Entry(lb)
    e.place(x=80,y=20)

    def Deletee():
        idd=e.get()
        if(idd==""):
            messagebox.showinfo("Error","Plese Fill Up...")
        else:
            con=sq.connect("my1.db")
            cur=con.cursor()
            cur.execute("delete from stud where id=?",(e.get()))
            con.commit()
            cur.close()
            con.close()
            e.delete(0,END)
            e.focus()
            messagebox.showinfo("message","Record Deleted...")
            top.destroy()
    btn1=Button(lb,text="Delete",command=Deletee)
    btn1.place(x=80,y=110)

    top.geometry("500x500")
    top.mainloop()

btn2=Button(f1,text="Delete",command=Delete_Record)
btn2.place(x=80,y=20)

btn2=Button(f1,text="Export",command=Edit_Record)
btn2.place(x=160,y=20)

root.geometry("500x500")
root.mainloop()