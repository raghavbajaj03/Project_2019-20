# PYTHON MODULE : BOOK
from datetime import date, datetime, timedelta
import sqlite3
import os
import platform
from db_utils import db_connect


def clrscreen():
     if platform.system()=="Windows":
        print(os.system("cls"))
     
def display():
    print("Inside display \n")
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        query = ("SELECT * FROM BookRecord")
        Cursor.execute(query)
        results=Cursor.fetchall()
        for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in results:
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Author of Book : ",Author)
            print("Price of Book : ",price)
            print("Publisher : ",publ)
            print("Total Quantity in Hand : ",qty)
            print("Purchased On : ",d_o_purchase)
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

def insertData():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        bno=input("Enter Book Code : ") 
        bname=input("Enter Book Name : ")
        Auth=input("Enter Book Author's Name : ")
        price=int(input("Enter Book Price : "))
        publ=input("Enter Publisher of Book : ")
        qty=int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/Month and Year seperately: ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        Qry = ("INSERT INTO BookRecord "\
               "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (bno,bname,Auth,price,publ,qty,date(YY,MM,DD))
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
          
def deleteBook():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        bno=input("Enter Book Code of Book to be deleted from the Library : ")

        Qry =("""DELETE FROM BookRecord WHERE Bno = ?""")
        del_rec=(bno,)
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

def SearchBookRec():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        bno=input("Enter Book No to be Searched from the Library : ")
        query = ("SELECT * FROM BookRecord where Bno = ? ")

        rec_srch=(bno,)
        Cursor.execute(query,rec_srch)

        Rec_count=0
        results=Cursor.fetchall()
        for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in results:
            Rec_count+=1
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Author of Book : ",Author)
            print("Price of Book : ",price)
            print("Publisher : ",publ)
            print("Total Quantity in Hand : ",qty)
            print("Purchased On : ",d_o_purchase)
            print("===============================================================")
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
    
def UpdateBook():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()


        bno=input("Enter Book Code of Book to be Updated from the Library : ")
        query = ("SELECT * FROM BookRecord where Bno = ? ")
        rec_srch=(bno,)
        Cursor.execute(query,rec_srch)
        
        for (Bno,Bname,Author,price,publ,qty,d_o_purchase) in Cursor:
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Author of Book : ",Author)
            print("Price of Book : ",price)
            print("Publisher : ",publ)
            print("Total Quantity in Hand : ",qty)
            print("Purchased On : ",d_o_purchase)
            print("===============================================================")

        print("\nEnter new data ")
        bname=input("Enter Book Name : ")
        Auth=input("Enter Book Author's Name : ")
        price=int(input("Enter Book Price : "))
        publ=input("Enter Publisher of Book : ")
        qty=int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date/MOnth and Year seperately: ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))


        Qry = ("UPDATE BookRecord SET bname=?,Author=?,"\
            "price=?,publisher=?,qty=?,d_o_purchase=? "\
              "WHERE Bno=?")
        data = (bname,Auth,price,publ,qty,date(YY,MM,DD),bno)


        Cursor.execute(Qry,data)
        # Make sure data is committed to the database'''
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Updated Successfully.............")
        
    except sqlite3.Error as err:
        print("Error while connecting to sqlite", err)

    finally:
        if (cnx):
            cnx.close()
            print("The SQLite connection is closed")