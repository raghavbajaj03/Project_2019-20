#PYTHON MODULE MEMBER
import sqlite3
from datetime import date, datetime, timedelta
import os
from db_utils import db_connect

def clrscreen():
    print('\n' *5)

def display():
    try:
        #print("\033[H\033[J")
        cnx = db_connect()
        Cursor = cnx.cursor()
        query = ("SELECT * FROM Member")
        Cursor.execute(query)
        results=Cursor.fetchall()
        
        for (Mno,Mname,MOB,DOP,ADR) in results:
            print("==============================================================")
            print("Member Code : ",Mno)
            print("Member Name : ",Mname)
            print("Mobile No.of Member : ",MOB)
            print("Date of Membership : ",DOP)
            print("Address : ",ADR)
            print("===============================================================")
            
            
        Cursor.close()
        cnx.close()
        print("You have done it!!!!!!")
        
    except sqlite3.Error as err:
        print("Error while connecting to sqlite", err)
        
    finally:
        if (cnx):
            cnx.close()
            print("The SQLite connection is closed")

                
                
                
                

def insertMember():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        mno=input("Enter Member Code : ")
        mname=input("Enter Member Name : ")
        mob=input("Enter Member Mobile No. : ")
        print("Enter Date of Membership (Date/MOnth and Year seperately: ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        addr=input("Enter Member Adress : ")
        Qry = ("INSERT INTO Member "\
                "VALUES (?, ?, ?, ?, ?)")
        data = (mno,mname,mob,date(YY,MM,DD),addr)
        Cursor.execute(Qry,data)
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted..............")
        
    except sqlite3.Error as err:
        print("Error while connecting to sqlite", err)
        
    finally:
        if (cnx):
            cnx.close()
            print("The SQLite connection is closed")

def deleteMember():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        mno=input("Enter Member Code to be deleted from the Library : ")

        Qry =("""DELETE FROM Member WHERE MNO = ?""")
        del_rec=(mno,)
        Cursor.execute(Qry,del_rec)

        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfully.............")

    except sqlite3.Error as err:
        print("Error while connecting to sqlite", err)
        
    finally:
        if (cnx):
            cnx.close()
            print("The SQLite connection is closed")

def SearchMember():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        mnm=input("Enter Member Name to be Searched from the Library : ")
        query = ("SELECT * FROM Member where MName = ? ")
        rec_srch=(mnm,)
        Cursor.execute(query,rec_srch)
        results=Cursor.fetchall()
        Rec_count=0
        for (Mno,Mname,MOB,DOP,ADR) in results:
            print("==============================================================")
            print("Member Code : ",Mno)
            print("Member Name : ",Mname)
            print("Mobile No.of Member : ",MOB)
            print("Date of Membership : ",DOP)
            print("Address : ",ADR)
            print("===============================================================")
            Rec_count+=1
        if Rec_count%2==0:
            input("Press any key to continue")
            clrscreen()
            print(Rec_count, "Record(s) found")
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()

    except sqlite3.Error as err:
        print("Error while connecting to sqlite", err)
        
    finally:
        if (cnx):
            cnx.close()
            print("The SQLite connection is closed")

def UpdateMember():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        mnm=input("Enter Member Name to be Searched from the Library : ")
        query = ("SELECT * FROM Member where MName = ? ")
        rec_srch=(mnm,)
        Cursor.execute(query,rec_srch)
        results=Cursor.fetchall()
        Rec_count=0
        for (Mno,Mname,MOB,DOP,ADR) in results:
            print("==============================================================")
            print("Member Code : ",Mno)
            print("Member Name : ",Mname)
            print("Mobile No.of Member : ",MOB)
            print("Date of Membership : ",DOP)
            print("Address : ",ADR)
            print("===============================================================")
            Rec_count+=1
        if Rec_count%2==0:
            input("Press any key to continue")
            clrscreen()
            print(Rec_count, "Record(s) found")
        # Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()

    except sqlite3.Error as err:
        print("Error while connecting to sqlite", err)
        
    finally:
        if (cnx):
            cnx.close()
            print("The SQLite connection is closed")