from tkinter import *
from tkinter import messagebox
import sqlite3 as sq

def CreateT():
    con=sq.connect("My.db")
    cur=con.cursor()
    cur.execute("create table if not exists Product(id integer primary key autoincrement,name text,price integer)")
    cur.close()
    con.close()
CreateT()

root=Tk()

lbframe=LabelFrame(root,text="For Insert Record",height=150,width=450)
lbframe.pack(fill="x")

lbl1=Label(lbframe,text="Name")
lbl1.place(x=20,y=20)
e1=Entry(lbframe)
e1.place(x=80,y=20)

lbl2=Label(lbframe,text="Price")
lbl2.place(x=20,y=50)
e2=Entry(lbframe)
e2.place(x=80,y=50)

def Insert_record():
    nm=e1.get()
    pr=e2.get()
    if(nm=="" or pr==""):
        messagebox.showinfo("Error","Please Enter Both Field...")
    else:
        con=sq.connect("My.db")
        cur=con.cursor()
        cur.execute("insert into Product(name,price)values(?,?)",(nm,pr))
        con.commit()
        cur.close()
        con.close()
        e1.delete(0,END)
        e2.delete(0,END)
        e1.focus()
        messagebox.showinfo("Successful","Record Inserted...")

btn1=Button(lbframe,text="Save",command=Insert_record)
btn1.place(x=90,y=80)

lb1=LabelFrame(root,text="For Search Record",height=100,width=450)
lb1.pack(fill="x")

lbl3=Label(lb1,text="Name")
lbl3.place(x=20,y=20)
e3=Entry(lb1)
e3.place(x=80,y=20)

def Insert_record():
    nm=e3.get()
    
btn1=Button(lb1,text="Search",command=Insert_record)
btn1.place(x=220,y=17)

lb2=LabelFrame(root,text="For View Records",height=200,width=450)
lb2.pack(fill="x")

def Edit_Record():
    top=Toplevel(root)
    top.title("Edit")
    lb=LabelFrame(top,text="Edit Record",height=300,width=450)
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

    btn1=Button(lb,text="Edit")
    btn1.place(x=80,y=110)

    top.geometry('500x500')
    top.mainloop()

f1=Frame(root,height=50,width=450)
f1.pack(fill="x")

btn2=Button(f1,text="Edit")
btn2.place(x=20,y=20)


btn2=Button(f1,text="Delete")
btn2.place(x=80,y=20)

btn2=Button(f1,text="Export Csv")
btn2.place(x=160,y=20)

root.geometry('500x500')
root.mainloop()