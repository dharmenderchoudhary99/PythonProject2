from tkinter import *
from tkinter import ttk
import requests

def get_city():
    city=city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e75cc1bdecbdc2542ef981c8947ebc61").json()
    w_Label1.config(text=data["weather"][0]["main"])
    wb_Label1.config(text=data["weather"][0]["description"])
    temp_Label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])
# city_name="jodhpur"
# data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=e75cc1bdecbdc2542ef981c8947ebc61").json()
# print(data)
# {'coord': {'lon': 73.03, 'lat': 26.2867},
# 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}],
# 'base': 'stations', 'main': {'temp': 306.49, 'feels_like': 304.11,
# 'temp_min': 306.49, 'temp_max': 306.49, 'pressure': 1015, 'humidity': 14,
# 'sea_level': 1015, 'grnd_level': 988}, 'visibility': 10000,
# 'wind': {'speed': 2.33, 'deg': 14, 'gust': 2.31}, 'clouds': {'all': 0},
# 'dt': 1677843568, 'sys': {'country': 'IN', 'sunrise': 1677807019, 'sunset': 1677848995},
# 'timezone': 19800, 'id': 1268865, 'name': 'Jodhpur', 'cod': 200}





win=Tk()
win.title("Weather Broadcast")
win.config(bg="blue")
win.geometry("500x570")

name_Label= Label(win, text="Weather App",font=("Times New Roman",30,"bold"))
name_Label.place(x=25,y=50,height=50,width=450)

list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
           "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh",
           "Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
           "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh",
           "Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh",
           "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep",
           "National Capital Territory of Delhi","Puducherry"]
city_name=StringVar()
com=ttk.Combobox(win,text="Weather Broadcast",values=list_name,font=("Times New Roman",20,"bold"),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)




w_Label= Label(win, text="Weather Climate",font=("Times New Roman",20))
w_Label.place(x=25,y=260,height=50,width=210)

w_Label1= Label(win, text="",font=("Times New Roman",20))
w_Label1.place(x=250,y=260,height=50,width=210)


wb_Label= Label(win, text="Weather Description",font=("Times New Roman",17))
wb_Label.place(x=25,y=330,height=50,width=210)

wb_Label1= Label(win, text="",font=("Times New Roman",17))
wb_Label1.place(x=250,y=330,height=50,width=210)

temp_Label= Label(win, text="Temperature",font=("Times New Roman",20))
temp_Label.place(x=25,y=400,height=50,width=210)

temp_Label1= Label(win, text="",font=("Times New Roman",20))
temp_Label1.place(x=250,y=400,height=50,width=210)

pre_label= Label(win, text="Weather Climate",font=("Times New Roman",20))
pre_label.place(x=25,y=470,height=50,width=210)

pre_label1= Label(win, text="",font=("Times New Roman",20))
pre_label1.place(x=250,y=470,height=50,width=210)

done_button=Button(win, text="Show",font=("Times New Roman",20,"bold"),command=get_city)
done_button.place(x=200,y=190,height=50,width=100)




win.mainloop()