import requests
import logging
import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.configure(bg='#B1D4E0')


logging.basicConfig(
    filename='logs/logging.log',
    level=logging.DEBUG,
    format='%(levelname)s %(asctime)s.%(msecs)03d - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
)

lb_str = StringVar()
lb_str.set('')

city = 'Amsterdam'
graden = u"\u2103"


def tk_exit():
    exit()


def tk_get_weather():
    r = requests.get('https://openweathermap.org/data/2.5/weather?appid=439d4b804bc8187953eb36d2a8c26a02')
    j = r.json()
    # print(j)
    # print(j['weather'][0])
    # print(j['weather'][0]['main'])
    # print(j['weather'][0]['description'])
    # print(j['main']['temp'])
    logging.info(f"Het weer voor {city} vandaag: {j['main']['temp']} {graden} en {j['weather'][0]['description']}")

    s = f"Het weer voor {city} vandaag: {j['main']['temp']} {graden} en {j['weather'][0]['description']}"
    lb_str.set(s)


root.title('Demo Openweathermap')
root.geometry('640x480')

label1 = tk.Label(root, text='Demo Openweathermap')
label1.pack(pady=5)

lb_openweathermap = tk.Label(root, relief=tk.SOLID, borderwidth=2, textvariable=lb_str)
lb_openweathermap.pack(pady=5)
lb_openweathermap.place(x=5, y=60, height=50, width=630)

get_weather_button = tk.Button(root, height=2, width=19, text='Update openweathermap', command=tk_get_weather)
get_weather_button.place(x=5, y=5)
# get_weather_button.pack()

exit_button = tk.Button(root, text='Exit', command=tk_exit)
exit_button.place(x=580, y=5)
# exit_button.pack()

root.mainloop()
