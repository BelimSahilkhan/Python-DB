from tkinter import ttk,filedialog
from tkinter import *
import pandas as pd #Used Csv Module To Change Pandas

def show_file():
    file_path= e1.get()
    delimiter = e2.get()
    header = cmd1.get()
    encoding = e3.get()

    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    e1.delete(0, END)
    e1.insert(0, file_path)

    if(header == "Yes"):
        header_val = 0
    else:
        header_val = None

    df = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding, header=header_val)

    txt1.delete("1.0",END)
    txt1.insert(END, df.to_string())
    
    #Csv Code
    """with open(file_path, "r", encoding=encoding, newline="") as f:
        reader = csv.reader(f, delimiter=delimiter)
        txt1.delete("1.0", END)
        if header == "No":
            next(reader)
        for i in reader:
            txt1.insert(END, str(i) + "\n")"""
def write_data():
    file_path=filedialog.asksaveasfilename(defaultextension=".csv")
    delimiter=e2.get()
    encoding=e3.get()
    get_data=txt1.get("1.0",END).split("\n")
    
    df=pd.DataFrame(get_data)
    df=df[0].str.split(",",expand=True)
    #df=df[0].str.split(",").apply(pd.Series)
    df.to_csv(file_path,index=False,header=False)
    
    #Csv Code
   # with open(file_path,"w",encoding=encoding,newline="")as f:
     #   writer=csv.writer(f,delimiter=delimiter)
        
       # for i in get_data:
         #   writer.writerow(i.split(","))"""
root=Tk()
root.geometry('500x500')

lb1=Label(root,text="Csv File")
lb1.place(x=10,y=10)

e1=Entry(root,width=45)
e1.place(x=80,y=10)

btn1=Button(root,text="Browse",command=show_file)
btn1.place(x=400,y=8)

lb2=Label(root,text="Delimiter:")

lb2.place(x=10,y=40)

e2=Entry(root)
e2.insert(0,",")
e2.place(x=80,y=40)

lb3=Label(root,text="Heading:")
lb3.place(x=10,y=70)
set_default_value=StringVar(value="Yes")
cmd1=ttk.Combobox(root,textvariable=set_default_value,values=["Yes","No"])
cmd1.place(x=80,y=70)


lb4=Label(root,text="Encoding:")
lb4.place(x=10,y=100)

e3=Entry(root)
e3.insert(0,"utf-8")
e3.place(x=80,y=100)

gp1=LabelFrame(root,text="Show Csv File Information")
gp1.place(x=30,y=200)
txt1=Text(gp1)
txt1.pack(padx=10,pady=10,expand=False)

bt3=Button(root,text="Write",command=write_data)
bt3.place(x=20,y=150)
root.mainloop()