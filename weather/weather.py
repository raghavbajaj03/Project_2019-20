import os
import platform
import sqlite3
import requests,json 
import PySimpleGUI as sg

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'SQLite_python.db')
IMG_PATH = os.path.join(os.path.dirname(__file__), 'images')
con=sqlite3.connect(DEFAULT_PATH)


############## Output Window ##############
def call_gui(ct,cp,ch,desc,img):
    #sg.theme('DarkAmber')  # No gray windows please!

    # STEP 1 define the layout
    layout = [ 
                [sg.Text('Temprature: {}'.format(ct))],
                [sg.Image(img)],
                [sg.Button('Button'), sg.Button('Exit')]
            ]

    #STEP 2 - create the window
    window = sg.Window('My new window', layout, grab_anywhere=True)

    # STEP3 - the event loop
    while True:
        event, values = window.read()   # Read the event that happened and the values dictionary
        print(event, values)
        if event in (None, 'Exit'):     # If user closeddow with X or if user clicked "Exit" button then exit
            break
        if event == 'Button':
            print('You pressed the button')
    window.close()



############## Login Screen ##############    
def LOGIN():
    user_id=""
    password=""
    if(con):
        mycursor=con.cursor()
    while(1):
        l=[]
        user_id=input('ENTER USER ID')
        l.append(user_id)
        # Check if user_id already exists
        find_user="SELECT user_id FROM user_details WHERE user_id=?;"
        mycursor.execute(find_user,(user_id,))
        results=mycursor.fetchone()
        if results:
            print(results)
            if(user_id==results[0]):
                    print("User already exists,plese pick another username\n")
        else:
            print("user not fount try again\n")
            continue
        password=input('ENTER PASSWORD')
        l.append(password)
        find_pass="SELECT password FROM user_details WHERE user_id=?;"
        #sql='INSERT INTO user_details( user_id, password) VALUES ( ?,? )'
        mycursor.execute(find_pass,(user_id,))
        results=mycursor.fetchone()
        if results:
            print(results)
            if(password==results[0]):
                    print("Credentials matched \n")
        else:
            print("Password mismatch, please try again\n")
            continue
        con.commit()
        print("Login Successful \n")
        break
    find_city1="SELECT city1 FROM user_details WHERE user_id=?;"
    mycursor.execute(find_city1,(user_id,))
    results=mycursor.fetchone()
    if results:
        print(results)
        show_city_info(results[0])
    con.close()

############## Sign Up Screen ############## 
def sign_up():
    if(con):
        mycursor=con.cursor()
    while(1):
        l=[]
        user_id=input('ENTER USER ID')
        l.append(user_id)
        # Check if user_id already exists
        find_user="SELECT user_id FROM user_details WHERE user_id=?;"
        mycursor.execute(find_user,(user_id,))
        results=mycursor.fetchone()
        if results:
            print(results)
            if(user_id==results[0]):
                    print("User already exists,plese pick another username\n")
                    continue
        else:
            print("not fount \n")
            password=input('ENTER PASSWORD')
            l.append(password)
            #sql='''insert into user_details(user_id,password) values('%s','%s');'''
            sql='INSERT INTO user_details( user_id, password) VALUES ( ?,? )'
            mycursor.execute(sql,(user_id,password))
            con.commit()
            print("Signup Successful \n")
        con.close()
        break

        
############## Showing City Details ############## 
def show_city_info(city):
    #api_key="cc9a28a7604bc8b3d0addd9b85ac8d21"
    #my api key
    api_key="ffed7bc78ee5dac9c811fd1393d88fc5"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city_name=city
    complete_url=base_url + "appid=" + api_key + "&q=" + city_name
    #complete_url="http://api.openweathermap.org/data/2.5/weather?"+"appid"+api_key+"&q"+city_name
    response=requests.get(complete_url)
    x=response.json()
    #print(x)
    if x["cod"]!="404":
        y=x["main"]
        current_temperature=y["temp"]
        current_pressure=y["pressure"]
        current_humidity=["humidity"]
        z=x["weather"]
        weather_description=z[0]["description"]
        print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description)) 
    else:
        print(" City Not Found ")
        
############## Guest Mode ############## 
def guest_mode():
    #api_key="cc9a28a7604bc8b3d0addd9b85ac8d21"
    #my api key
    api_key="ffed7bc78ee5dac9c811fd1393d88fc5"
    base_url="http://api.openweathermap.org/data/2.5/weather?"
    city_name=input("Enter City Name:")
    complete_url=base_url + "appid=" + api_key + "&q=" + city_name
    #complete_url="http://api.openweathermap.org/data/2.5/weather?"+"appid"+api_key+"&q"+city_name
    response=requests.get(complete_url)
    x=response.json()
    #print(x)
    if x["cod"]!="404":
        y=x["main"]
        ct=y["temp"]-273.15
        cp=y["pressure"]
        ch=["humidity"]
        z=x["weather"]
        desc=z[0]["description"]
        img=IMG_PATH+'/10d@2x.png'

        print(" Temperature (in degree celcius) = " +
                    str(ct) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(cp) +
          "\n humidity (in percentage) = " +
                    str(ch) +
          "\n description = " +
                    str(desc)) 
        call_gui(ct,cp,ch,desc,img)
    else:
        print(" City Not Found ") 
   
############## Main Menu ##############      
def MenuSet():
    runAgn ='y'
    while(runAgn.lower() == 'y'):
        print('ENTER NUMBER')
        print('1.LOGIN')
        print('2.SIGN_UP')
        print('3.CITY WEATHER')
        ch=int(input('ENTER YOUR CHOICE\n'))
        if ch==1:
            LOGIN()
        elif ch==2:
            sign_up()
        elif ch==3:
            guest_mode()
        else:
            print("Wrong input try again\n")
            if(platform.system() == "Windows"):
                print(os.system('cls'))
            else:
                print(os.system('clear'))
        runAgn = input("\n want To Run Again Y/n: ")

############## Start from here ############## 
MenuSet()