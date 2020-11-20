import PIL
import requests
from datetime import datetime
import tkinter as Tk
from tkinter import *
from tkinter import simpledialog ,messagebox


#weather app data
def weather_app():
        location = str(en1.get())

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
        api_address= "http://api.openweathermap.org/data/2.5/weather?appid=4d5c07cefc1bd6ffd727c23d9fd03ea5&q="
        url = api_address + location

        json_data= requests.get(url).json()
#function to display data and extract the relevant data from the json file.

        if json_data ['cod'] == '404':
                print("Invalid City: {} Please check your city name".format(location))
        else:
    #create variables to store and display jaosn data
         temp_city = ((json_data['main']['temp'])-273.15) #kelvin - 273.15 gives us the tempreture in celcius
         weather_desc = json_data['weather'][0]['description']
         hmdt= json_data['main']['humidity']
         wnd_spd= json_data['wind']['speed']
         date_time=datetime.now().strftime ("%d %b %Y | %I %M %S %p")
        lb2.config(text=str("Weather Stats for - {} | {}".format(location.upper(), date_time)))
        lb3.config(text=str("Current Weather Description:" + str( weather_desc)))
        lb4.config(text=str("Current Humidity :"+ str(hmdt)+"%"))
        lb5.config(text=str("Current Temperature is: {:.2f}\N{DEGREE SIGN}C ".format(temp_city)))
        lb6.config(text=str("Current Wind Speed:" + str(wnd_spd)+ "kmph"))

        if temp_city > 15:
            master.configure(bg="orange")
        else:
            master.configure(bg="powder blue")

master= Tk()
master.title('Weather App')
master.config(bg="cadet blue", relief="solid")
master.geometry("700x600")



lbheading = Label(master, text="My Weather App" ,font="arial 22 bold", bg='powderblue')
lbheading.pack()

lb1 = Label(master,text="Enter City:", font='arial 18 bold')
lb1.pack(pady=20)


en1= Entry(master)
en1.pack(pady=20)

checkbutton = Button(master, text="Search",font= "bold", command=weather_app)
checkbutton.pack(pady=20)

lb2 = Label(master, font="arial 16", bg="cadet blue")
lb2.pack(pady=20)

lb3 = Label(master,  font="arial 14", bg="cadet blue")
lb3.pack(pady=20)

lb4 = Label(master,  font="arial 14", bg="cadet blue")
lb4.pack(pady=20)

lb5 = Label(master, font="arial 14", bg="cadet blue")
lb5.pack(pady=20)

lb6 = Label(master, font="arial 14", bg="cadet blue")
lb6.pack(pady=20)


master.mainloop()
