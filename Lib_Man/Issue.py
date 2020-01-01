#PYTHON MODULE : ISSUE
import sqlite3
from datetime import date
import os
from db_utils import db_connect


def clrscreen():
    print('\n' *5)

def ShowIssuedBooks():
    try:
        #print("\033[H\033[J")
        cnx = db_connect()
        Cursor = cnx.cursor()
        query = ("SELECT B.bno,bname,M.mno,mname,d_o_issue,d_o_ret FROM bookRecord B,issue I"\
                 ",member M where B.bno=I.bno and I.mno=M.mno")
        Cursor.execute(query)
        
        
        for (Bno,Bname,Mno,Mname,doi,dor) in Cursor:
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Member Code : ",Mno)
            print("Member Name : ",Mname)
            print("Date of issue : ",doi)
            print("Date of return : ",dor)

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


def issueBook():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()

        bno=input("Enter Book Code to issue : ")
        mno=input("Enter Member Code : ")
        print("Enter Date of Issue (Date/MOnth and Year seperately: ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        

        Qry = ("INSERT INTO issue (bno,mno,d_o_issue)"\
               "VALUES (?,?,?)")
        data = (bno,mno,date(YY,MM,DD))
        Cursor.execute(Qry,data)
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
               
            
def returnBook():
    try:
        cnx = db_connect()
        Cursor = cnx.cursor()
        
        
        bno=input("Enter Book Code of Book to be returned to the Library : ")
        Mno=input("Enter Member Code of Member who is returning Book : ")
        retDate=date.today()
        Qry =("""Update Issue set d_o_ret=? WHERE BNO = ? and Mno= ? """)
        rec=(retDate,bno,Mno)
        Cursor.execute(Qry,rec)

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