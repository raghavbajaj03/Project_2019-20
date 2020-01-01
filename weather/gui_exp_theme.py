import os
import platform
import sqlite3
import requests,json 
import PySimpleGUI as sg
from datetime import datetime
from pyowm import OWM
import datetime
 
currentDT = datetime.datetime.now()
 
print (currentDT.strftime("%Y-%m-%d %H:%M:%S"))
print (currentDT.strftime("%Y/%m/%d"))
print (currentDT.strftime("%H:%M:%S"))
print (currentDT.strftime("%I:%M:%S %p"))
print (currentDT.strftime("%a, %b %d, %Y"))

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'SQLite_python.db')
IMG_PATH = os.path.join(os.path.dirname(__file__), 'images')


############## Output Window ##############
def call_gui(city_name,ct,cp,ch,desc,img):
    #sg.theme('DarkAmber')  # No gray windows please!

    # STEP 1 define the layout
    layout = [ 
                [sg.Text('{}'.format(city_name))],
                [sg.Text(currentDT.strftime(" %d %B,%Y  %A "))],
                [sg.Text(currentDT.strftime("%H:%M:%S"))],
                [sg.Text('Pressure: {}'.format(cp))],
                [sg.Text('Humidity: {}'.format(ch))],
                [sg.Image(img)],
                [sg.Text(desc)],
                #print("{0:.2f}".format(a))
                [sg.Text('{0:.2f} Degree Celcius'.format(ct))],
                [sg.Button('Exit')]
             ]
   #STEP 2 - create the window
    window = sg.Window('Tempy', layout, no_titlebar=False, alpha_channel=.9,grab_anywhere=True)

    # STEP3 - the event loop
    while True:
        event, values = window.Read()   # Read the event that happened and the values dictionary
        print(event, values)
        if event in (None, 'Exit'):     # If user closeddow with X or if user clicked "Exit" button then exit
            break
    window.Close()



############## Guest Mode 1 ##############
def guest_mode():
    #api_key="cc9a28a7604bc8b3d0addd9b85ac8d21"
    #my api key
    api_key="ffed7bc78ee5dac9c811fd1393d88fc5"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city_name=input("Enter City Name: ")
    complete_url=base_url + "appid=" + api_key + "&q=" + city_name
    #complete_url="http://api.openweathermap.org/data/2.5/weather?"+"appid"+api_key+"&q"+city_name
    response=requests.get(complete_url)
    x=response.json()
    print(x)
    if x["cod"]!="404":
        y=x["main"]
        ct=y["temp"]-273.15
        cp=y["pressure"]
        ch=y["humidity"]
        z=x["weather"]
        desc=z[0]["description"]
        w=z[0]["icon"]
        print(w)
        img=IMG_PATH+'/'+w+'@2x.png'

        print(" Temperature (in degree celcius) = " +
                    str(ct) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(cp) +
          "\n humidity (in percentage) = " +
                    str(ch) +
          "\n description = " +
                    str(desc)) 
        call_gui(city_name,ct,cp,ch,desc,img)
    else:
        print(" City Not Found ") 

############## Guest Mode 2 ##############
def guest_mode2():
    # uses pyowm
    # to know more visit the link below
    # https://pyowm.readthedocs.io/en/latest/usage-examples-v2/weather-api-usage-examples.html

    api_key="ffed7bc78ee5dac9c811fd1393d88fc5"
    owm = OWM(api_key)
    city_name=input("Enter the city: ")
    obs = owm.weather_at_place(city_name)
    w = obs.get_weather()
    t=w.get_temperature(unit='celsius')
    #{'temp': 10.54, 'temp_max': 10.54, 'temp_min': 10.54, 'temp_kf': None}
    print("Current temp = {} degree celsius".format(t['temp'])) 
    



############## Main Menu ##############      
def MenuSet():
    runAgn ='y'
    while(runAgn.lower() == 'y'):
        print('ENTER NUMBER')
        print('1.LOGIN')
        print('2.SIGN_UP')
        print('3.CITY WEATHER')
        print('4. New Guest mode')
        ch=int(input('ENTER YOUR CHOICE\n'))
        if ch==1:
            pass
        elif ch==2:
            pass
        elif ch==3:
            guest_mode()
        elif ch==4:
            guest_mode2()
        else:
            print("Wrong input try again\n")
        '''
        if(platform.system() == "Windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        '''
        runAgn = input("\n want To Run Again Y/n: ")

############## Start from here ############## 
MenuSet()