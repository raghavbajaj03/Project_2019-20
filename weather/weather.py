import os
import platform
import sqlite3
import requests,json 
import PySimpleGUI as sg
from datetime import datetime

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


############## Login Screen ##############    
def LOGIN():
    con=sqlite3.connect(DEFAULT_PATH)
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
    display_city(user_id)
    modify_city(user_id)
    con.close()
    
def modify_city(user_id):
    con=sqlite3.connect(DEFAULT_PATH)
    if(con):
        mycursor=con.cursor()
    ch=input("Enter Choice y/n\n")
    if ch=='y':
        print("If you want to change city1 enter 1")
        print("If you want to change city2 enter 2")
        print("If you want to change city3 enter 3")
        a=int(input("Enter your choice"))
        if(a==1):
            city1=input("Enter the name of new city in place of city1 : ")
            val=(city1,user_id)
            sql="update user_details set city1=? where user_id=?;"
            mycursor.execute(sql,val)
            con.commit()
        elif(a==2):
            city2=input("Enter the name of new city in place of city1 : ")
            val=(city2,user_id)
            sql="update user_details set city1=? where user_id=?;"
            mycursor.execute(sql,val)
            con.commit()
        elif(a==3):
            city3=input("Enter the name of new city in place of city1 : ")
            val=(city3,user_id)
            sql="update user_details set city1=? where user_id=?;"
            mycursor.execute(sql,val)
            con.commit()
    con.close()
                 
def display_city(user_id):
    con=sqlite3.connect(DEFAULT_PATH)
    if(con):
        mycursor=con.cursor()
    find_city1="SELECT city1 FROM user_details WHERE user_id=?;"
    print("Getting the user id again from table ",user_id)
    mycursor.execute(find_city1,(user_id,))
    results=mycursor.fetchone()
    if(results[0]==None):
        city1=input("Kindly add city1 as it was not found in saved choice \n")
        val=(city1,user_id)
        sql="update user_details set city1=? where user_id=?;"
        mycursor.execute(sql,val)
        con.commit()
        find_city1="SELECT city1 FROM user_details WHERE user_id=?;"
        mycursor.execute(find_city1,(user_id,))
        results=mycursor.fetchone()
        con.commit()
        print(results)
    else:
        print(results)
        show_city_info(results[0])
        
        
    find_city2="SELECT city2 FROM user_details WHERE user_id=?;"
    print("Getting the user id again from table ",user_id)
    mycursor.execute(find_city2,(user_id,))
    results=mycursor.fetchone()
    if(results[0]==None):
        city2=input("Kindly add city2 as it was not found in saved choice \n")
        val=(city2,user_id)
        sql="update user_details set city2=? where user_id=?;"
        mycursor.execute(sql,val)
        con.commit()
        find_city1="SELECT city2 FROM user_details WHERE user_id=?;"
        mycursor.execute(find_city2,(user_id,))
        results=mycursor.fetchone()
        con.commit()
        print(results)
    else:
        print(results)
        show_city_info(results[0])
    
        
    find_city3="SELECT city3 FROM user_details WHERE user_id=?;"
    print("Getting the user id again from table ",user_id)
    mycursor.execute(find_city3,(user_id,))
    results=mycursor.fetchone()
    if(results[0]==None):
        city3=input("Kindly add city3 as it was not found in saved choice \n")
        val=(city3,user_id)
        sql="update user_details set city3=? where user_id=?;"
        mycursor.execute(sql,val)
        con.commit()
        find_city1="SELECT city3 FROM user_details WHERE user_id=?;"
        mycursor.execute(find_city3,(user_id,))
        results=mycursor.fetchone()
        con.commit()
        print(results)
    else:
        print(results)
        show_city_info(results[0])
        
           
    print("Do you wish to update city\n")
    print(input("\n Enter Your Choice Y/n"))
    
    con.close()

############## Sign Up Screen ############## 
def sign_up():
    con=sqlite3.connect(DEFAULT_PATH)
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
        current_humidity=y["humidity"]
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