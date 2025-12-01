from tkinter import *;
from tkinter import messagebox,ttk;
import sqlite3 as sq
root = Tk();
root.title("School System");
data = "";

# ---------- DATABASE ----------
def init():
    cnn = sq.connect("My.db");
    cursor = cnn.cursor();
    cursor.execute("create table if not exists student_record(id integer primary key autoincrement,student_name text,class_name text)")
    cursor.close();
    cnn.close();
init();


def insert_data():
    try:
        cls = txt1.get(txt1.curselection())   
    except:
        messagebox.showwarning("Warning", "Please select a Class")
        return

    nm = txt2.get().strip()   

    if(nm == ""):
        messagebox.showwarning("Warning", "Please enter Student Name")
        return

    cnn = sq.connect("My.db");
    cursor = cnn.cursor();
    cursor.execute("insert into student_record(student_name,class_name) values(?,?)", (nm, cls))
    
    cnn.commit()
    last_id = cursor.lastrowid
    cursor.close()
    cnn.close()

    txt1.selection_clear(0, END)
    txt2.delete(0, END)
    txt2.focus()

    messagebox.showinfo("Information", "Student Added Successfully!")

    data.insert("", END, values=(last_id, nm, cls))


gp1 = LabelFrame(root, text="Register Student", width="800", height="200")
gp1.pack(padx=150, pady=10, fill="x", expand=False)

gp3 = LabelFrame(root, text="All Student Records", width="800", height="500")
gp3.pack(padx=350, pady=10, fill="x", expand=False)


def display():
    cnn = sq.connect("My.db");
    cursor = cnn.cursor();
    cursor.execute("select * from student_record")
    rows = cursor.fetchall()

    global data
    data = ttk.Treeview(gp3, columns=["id", "student_name", "class_name"], show="headings")
    data.heading("id", text="ID")
    data.heading("student_name", text="Student Name")
    data.heading("class_name", text="Class")

    for row in rows:
        data.insert("", END, values=row)

    data.pack(expand=True, fill="both", padx=10, pady=10)
    cursor.close();
    cnn.close()

display()


lbl2 = Label(gp1, text="Student Name")
lbl2.place(x=30, y=10)
txt2 = Entry(gp1)
txt2.place(x=150, y=10)

lbl1 = Label(gp1, text="Select Class")
lbl1.place(x=30, y=45)

txt1 = Listbox(gp1, height=6)
class_list = [
    "Class 1", "Class 2", "Class 3", "Class 4", "Class 5",
    "Class 6", "Class 7", "Class 8", "Class 9", "Class 10",
    "Class 11", "Class 12"
]
for c in class_list:
    txt1.insert(END, c)

txt1.place(x=150, y=45)

btn1 = Button(gp1, text="Save Student", command=insert_data)
btn1.place(x=100, y=150)

root.geometry("5020x750")
root.mainloop()