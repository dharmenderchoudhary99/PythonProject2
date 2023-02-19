from tkinter import *
from tkinter import ttk

from googletrans import Translator,LANGUAGES

def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans = Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1

def data():
    s=comb1_sor.get()
    d=comb1_dest.get()
    masg=sor_text.get(1.0,END)
    textget= change(text=masg,src=s,dest=d)
    des_text.delete(1.0,END)
    des_text.insert(END,textget)




root=Tk()
root.title("Google Translator")
root.geometry("500x700")
root.config(bg="red")

label_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"))
label_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_text=Label(root,text="Source Text",font=("Times New Roman",20,"bold"),fg="black",bg="red")
lab_text.place(x=100,y=100,height=20,width=300)

sor_text=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
sor_text.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb1_sor = ttk.Combobox(frame,values=list_text)
comb1_sor.place(x=10,y=300,height=40,width=150)
comb1_sor.set("english")


button_change=Button(frame,text="Translate",relief=RAISED,command=data)
button_change.place(x=170,y=300,height=40,width=150)

comb1_dest = ttk.Combobox(frame,values=list_text)
comb1_dest.place(x=330,y=300,height=40,width=150)
comb1_dest.set("Hindi")


label_txt=Label(root,text="Dest Text",font=("Time New Roman",20,"bold"),fg="black",bg="red")
label_txt.place(x=100,y=360,height=20,width=300)

des_text=Text(frame,font=("Times New Roman",20,"bold"),wrap=WORD)
des_text.place(x=10,y=400,height=150,width=480)

root.mainloop()