import pyautogui
from tkinter import *


# ss=pyautogui.screenshot()
# ss.save("test1.png")
def take_ss():
    add_data=entry.get()
    path=add_data+"\\test.png"
    print(path)
    ss=pyautogui.screenshot()
    ss.save("test1.png")
win=Tk()
win.title("ScreenShot")
win.geometry("700x400")
win.config(bg="yellow")
win.resizable(False,False)

entry=Entry(win,font=("Times New Roman",40))
entry.place(x=20,y=50,height=70,width=660)

bttn = Button(win, text="Done",font=("Times New Roman",50),command=take_ss)
bttn.place(x=250,y=140,height=100,width=200)



win.mainloop()

# to bild app go to folder
# where the file is there and run cmd
# and type pyinstaller --onefile (filename.py)