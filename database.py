#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:49:17 2018

@author: bishal
"""

import MySQLdb


def insert_Update(Bill_No,C_Name,Table_No,Address,Date,Total_Cost):
    database = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="Bishal",         # your username
                     passwd="*Incorrect@7012#",  # your password
                     database="Manakamana")        # name of the data base

    cursor = database.cursor()

    Command = "SELECT * from IceCream where Bill_No=" + str(Bill_No)
    cursor.execute(Command)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        Command = "UPDATE IceCream SET C_Name" + str(C_Name)+"WHERE Bill_No="+str(Bill_No)
    else:
        Command = "INSERT INTO IceCream(Bill_No,C_Name,Table_No,Address,Date,Total_Cost) VALUES("+str(Bill_No)+","+str(C_Name)+","+str(Table_No)+","+str(Address)+","+str(Date)+","+str(Total_Cost)+")"
        
    cursor.execute(Command)
   #for row in cursor.fetchall():
       #print (row[0])
       #print (row[3])
    database.commit()
    database.close()
    
    
bill_no=str(input("Enter the bill no:"))
c_name=str(input("Enter the customer name:"))
table_no = str(input("Enter the table number:"))
address = str(input("Enter the address:"))
date= str(input("Enter the date:"))
total_cost = str(input("Enter the total cost:"))

insert_Update(bill_no,c_name,table_no,address,date,total_cost)
