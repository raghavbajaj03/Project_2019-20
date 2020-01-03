import sqlite3
import os
import platform
from datetime import date
import site

import sys

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'SQLite.Python.db')

mydb=sqlite3.connect(DEFAULT_PATH)
mycursor=mydb.cursor()

sqlite_createtable_query='''create table IF NOT EXISTS parkmaster11
                           (vid INTEGER NOT NULL PRIMARY KEY,
                            pname VARCHAR(21),
                            vname VARCHAR(21),
                            level1 VARCHAR(11),
                            freespace1 VARCHAR(5),
                            vehicleno1 VARCHAR,
                            nod1 INTEGER,
                            vehtype INTEGER,
                            perdaycharge INTEGER
                            dateofpark TEXT,
                            payment1 INTEGER,
                            mobile_no INTEGER
                            );
'''
mycursor.execute(sqlite_createtable_query)

def add__record():
#mycursor.commit()
    l=[]
    vid=int(input('enter the parking number: '))
    l.append(vid)
    pname=input('enter person\'s name: ')
    l.append(pname)
    vname=input('enter vehicle model name: ')
    l.append(vname)
    
    level1=input('enter the level of parking:')
    l.append(level1)
    freespace1=input('is there any freespace or not: YES/NO ')
    l.append(freespace1)
    vehicleno1=int(input('enter the vehicle number: '))
    l.append(vehicleno1)
    nod1=int(input('enter total no. of days of parking: '))
    l.append(nod1)
    print('Select vehicle type:')
    vehtype=input('enter vehicle type car/bike/cycle/auto/bus/truck \n: ')
    if vehtype=='car':
        vt=4
        perdaycharge=250
    elif vehtype=='bike':
        perdaycharge=150
        vt=2
    elif vehtype=='cycle':
        perdaycharge=50
        vt=1
    elif vehtype=='auto':
        perdaycharge=250
        vt=3
    elif vehtype=='bus':
        perdaycharge=350
        vt=6
    elif vehtype=='truck':
        perdaycharge=300
        vt=5
    l.append(vt)
    l.append(perdaycharge)
    li_dt=input('enter in format dd-mm-yyyy').split("-")
    dateofpark=date(int(li_dt[2]),int(li_dt[1]),int(li_dt[0]))
    l.append(dateofpark)
    payment1=perdaycharge*nod1
    l.append(payment1)
    mobile_no=int(input('enter mobile no'))
    l.append(mobile_no)
    stud=(l)
    sql='insert into parkmaster11(vid,pname,vname,level1,freespace1,vehicleno1,nod1,vehtype,perdaycharge,dateofpark,payment1,mobile_no)values(?,?,?,?,?,?,?,?,?,?,?,?)'
    mycursor.execute(sql,stud)
    mydb.commit()
    print('-----------------------------------------------------------------------------------------------')
    print('                               YOUR PARKING RECEIPT                                          ')
    print('-----------------------------------------------------------------------------------------------')
    print(' DATE:                                                                          ',dateofpark)
    print(' YOUR PARKING NO.:                                                              ',vid)
    print(u' YOUR NAME:                                                                     ',repr(pname))
    print(u' YOUR VEHICLE NAME:                                                             ',repr(vname))
    print(' YOUR VEHICLE NO.:                                                              ',vehicleno1)
    print(' PER DAY CHARGE:                                                                ',perdaycharge)
    print(' NUMBER OF DAYS:                                                                ',nod1)    
    print('-----------------------------------------------------------------------------------------------')
    print(' YOUR PAYMENT:                                                                  ',payment1)
    print('-----------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------')
    print('                                      COME AGAIN :)                                          ')
    print('-----------------------------------------------------------------------------------------------')

    
def parking_table_view():
    print('select the search criteria:')
    print('1.Parking Number')
    print('2.Parking Name')
    print('3.Level No.')
    print('4.Vehicle No.')
    print('5.Date of Parking')
    print('6.All')
    ch= int(input('enter the choice:' ))
    if ch==1:
        s=int(input('enter parking no: '))
        rl=(s,)
        sql='select * from parkmaster11 where vid=?'
        mycursor.execute(sql,rl)
    elif ch==2:
        s=input('enter parking name: ')
        rl=(s,)
        sql='select * from parkmaster11 where pname=?'
        mycursor.execute(sql,rl)
    elif ch==3:
        s=int(input('enter level of parking: '))
        rl=(s,)
        sql='select * from parkmaster11 where level1=?'
        mycursor.execute(sql,rl)
    elif ch==4:
        s=int(input('enter vehicle no.: '))
        rl=(s,)
        sql='select * from parkmaster11 where vehicleno1=?'
        mycursor.execute(sql,rl)
    elif ch==5:
        s=date('enter date of parking in format(year,month,day): ')
        rl=(s,)
        sql='select * from parkmaster11 where dateofpark=?'
        mycursor.execute(sql,rl)
    elif ch==6:
        sql='select * from parkmaster11'
        mycursor.execute(sql)

    res=mycursor.fetchall()
    print('DETAILS about parking are as follows:')
    print('Parking ID,Parking Name,Level,FreeSpace(Y/N),Vehicle No.,No. of days for parking,Payment')
    for x in res:
        print(repr(x))

def checkout():
    vid=int(input('enter vid from receipt: '))
    s=(vid,)
    sql='select * from parkmaster11 where vid=?'
    mycursor.execute(sql,s)  
    res=mycursor.fetchone()
    li_pkdt=res[10].split("/")
    datepark=date(int(li_pkdt[2]),int(li_pkdt[1]),int(li_pkdt[0]))
    li_dt=input('enter in format dd-mm-yyyy').split("-")
    dateofpick=date(int(li_dt[2]),int(li_dt[1]),int(li_dt[0]))
    diff=dateofpick-datepark
    diff=diff.days
    vehtype=input('enter vehicle type car/bike/cycle/auto/bus/truck \n')
    if vehtype=='car':
        perdaycharge=250
    elif vehtype=='bike':
        perdaycharge=150
    elif vehtype=='cycle':
        perdaycharge=50
    elif vehtype=='auto':
        perdaycharge=250
    elif vehtype=='bus':
        perdaycharge=350
    elif vehtype=='truck':
        perdaycharge=300
    penalty=diff*perdaycharge
    #penalty=0
    payment=res[9]
    total_payment=penalty+payment
    print('-----------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------')        
    print('                               ARROGANT SAMURAI PARKING SERVICES                                          ')
    print('-----------------------------------------------------------------------------------------------')
    print('  DATE:                                                                          ',dateofpick)
    print(' YOUR PARKING NO.:                                                               ',res[0])
    print(u' YOUR NAME:                                                                      ',repr(res[1]))
    print(u' YOUR VEHICLE NAME:                                                              ',repr(res[2]))
    print(' YOUR VEHICLE NO.:                                                               ',res[5])
    print(' PER DAY CHARGE:                                                                 ',res[8])
    print(' NUMBER OF DAYS:                                                                 ',res[6])
    print('')
    print('-----------------------------------------------------------------------------------------------')
    print(' YOUR PAYMENT:                                                                   ',payment)
    print(' YOUR PENALTY:                                                                   ',penalty)
    print('-----------------------------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------------------------')
    print('YOUR TOTAL PAYMENT:                                                              ',total_payment )
    print('-----------------------------------------------------------------------------------------------')
    print('                                      COME AGAIN :)                                            ')
    print('-----------------------------------------------------------------------------------------------')

def remove():
    print('REMOVE CRIETERIA')
    print('1. Parking No.')
    print('2. Parking Name')
    print('3. Vehicle No.')
    ch=int(input("Your Choice is: "))
    if ch==1:
        vid=int(input('enter the Parking No. of the vehicle which was alloted to the person: '))
        rl=(vid,)
        sql='delete from vehicle where vid=?'
        mycursor.execute(sql,rl)
        mydb.commit()
    elif ch==2:
        pname=input('enter the person Name : ')
        rl=(pname,)
        sql='delete from vehicle where pname=?'
        mycursor.execute(sql,rl)
        mydb.commit()
    elif ch==3:
        vehicleno1=int(input('enter the vehicle no. of the vehicle whose details is to be viewed: '))
        rl=(vehicleno1,)
        sql='delete from vehicle where vehicleno1=?'
        mycursor.execute(sql,rl)
        mydb.commit()

def Menu():
    while(1):
        print('ENTER 1:TO ADD PARKING DETAIL')
        print('ENTER 2:TO VIEW PARKING DETAIL')
        print('ENTER 3:TO FINAL RECEIPT')
        print('ENTER 4:TO REMOVE  RECORD')
        print('ENTER 5:TO Exit')
        option=int(input('please select an above option: '))
        if option==1:
            add__record()
        if option==2:
            parking_table_view()
        if option==3:
            checkout()
        if option==4:
            remove()
        if option==5:
            break
        else:
            #print("Please try again \n")
            """
            if(platform.system()=='Windows'):
                print(os.system('cls'))
            else:
                print(os.system('clear'))
            """
Menu()
mycursor.close()
mydb.close()
