from tkinter import *
import speedtest


def speedcheck():
    sp=speedtest.Speedtest()
    sp.get_servers()
    down=str(round(sp.download()/(10**6),3))+"Mbps"
    up=str(round(sp.upload()/(10**6),3))+"Mbps"
    lab_d.config(text=down)
    lab_u.config(text=up)



sp=Tk()
sp.title("Speed Testing")
sp.geometry("500x700")
sp.config(bg="Blue")

lab=Label(sp,text="Internet Speed Test",font=("Time New Roman",30,"bold"),bg="Blue",fg="White")
lab.place(x=60,y=40,height=50,width=380)


lab=Label(sp,text="Download Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=130,height=50,width=380)

lab_d=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_d.place(x=60,y=200,height=50,width=380)

lab=Label(sp,text="Upload Speed",font=("Time New Roman",30,"bold"))
lab.place(x=60,y=290,height=50,width=380)

lab_u=Label(sp,text="00",font=("Time New Roman",30,"bold"))
lab_u.place(x=60,y=360,height=50,width=380)


btn = Button(sp,text="CHECK SPEED",font=("Time New Roman",30,"bold"),relief=RAISED,bg="Red",command=speedcheck)
btn.place(x=60,y=460,height=50,width=380)


sp.mainloop()
