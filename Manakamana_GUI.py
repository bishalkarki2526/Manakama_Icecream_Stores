from tkinter import *
from tkinter import ttk
import random
import datetime
import time;
import tkinter.messagebox
from math import sqrt as sqr
import MySQLdb

root=Tk()
root.geometry("1350x750+0+0")
root.title("Manakamana Icecream Stores")
root.configure(background="blue")
#===========================Frames==============================================================================

Tops=Frame(root, width=1380, height=80, bd=2, relief="raise")
Tops.pack(side=TOP)

F1=Frame(root, width=1050, height=660, bd=2, relief="raise")
F1.pack(side=LEFT)
F2=Frame(root, width=300, height=660, bd=2, relief="raise")
F2.pack(side=RIGHT)

F1a=Frame(F1, width=1000, height=330, bd=2, relief="raise")
F1a.pack(side=TOP)
F1b=Frame(F1, width=1000, height=320, bd=2, relief="raise")
F1b.pack(side=BOTTOM)

F2a=Frame(F2, width=300, height=450, bd=2, relief="raise")
F2a.pack(side=TOP)
F2b=Frame(F2, width=300, height=250, bd=2, relief="raise")
F2b.pack(side=BOTTOM)

F1aa=Frame(F1a, width=353, height=330, bd=2, relief="raise")
F1aa.pack(side=LEFT)
F1bb=Frame(F1a, width=353, height=330, bd=2, relief="raise")
F1bb.pack(side=LEFT)
F1cc=Frame(F1a, width=353, height=330, bd=2, relief="raise")
F1cc.pack(side=RIGHT)

F2aa=Frame(F1b, width=353, height=330, bd=2, relief="raise")
F2aa.pack(side=LEFT)
F2bb=Frame(F1b, width=353, height=330, bd=2, relief="raise")
F2bb.pack(side=LEFT)
F2cc=Frame(F1b, width=353, height=330, bd=2, relief="raise")
F2cc.pack(side=RIGHT)
#===================================================================================================================

Tops.configure(background="blue")
F1.configure(background="blue")
F2.configure(background="blue")

lblInfo=Label(Tops, font=('arial',30,'bold'), text="\t\t Manakamana Ice-Cream Stores \t\t", bd=2,anchor='w')
lblInfo.grid(row=0, column=0)
#==================================Variable Declaration==============================================================
def chkbutton_Value():
    if (var1.get() == 1):
        txtCherry_Ice_Cream.configure(state=NORMAL)
    elif var1.get() == 0:
        txtCherry_Ice_Cream.configure(state=DISABLED)
        E_Cherry_Ice_Cream.set("0")
    if (var2.get() == 1):
        txtCandy_Cone_Ice_Cream.configure(state=NORMAL)
    elif (var2.get() == 0):
        txtCandy_Cone_Ice_Cream.configure(state=DISABLED)
        E_Candy_Cone_Ice_Cream.set("0")
    if (var3.get() == 1):
        txtChocolate_Ice_Cream.configure(state=NORMAL)
    elif (var3.get() == 0):
        txtChocolate_Ice_Cream.configure(state=DISABLED)
        E_Chocolate_Ice_Cream.set("0")
    if (var4.get() == 1):
        txtVanilla_Ice_Cream.configure(state=NORMAL)
    elif (var4.get() == 0):
        txtVanilla_Ice_Cream.configure(state=DISABLED)
        E_Vanilla_Ice_Cream.set("0")
    if (var5.get() == 1):
        txtButter_Scotch_Ice_Cream.configure(state=NORMAL)
    elif (var5.get() == 0):
        txtButter_Scotch_Ice_Cream.configure(state=DISABLED)
        E_Butter_Scotch_Ice_Cream.set("0")
    if (var6.get() == 1):
        txtStrawberry_Ice_Cream.configure(state=NORMAL)
    elif (var6.get() == 0):
        txtStrawberry_Ice_Cream.configure(state=DISABLED)
        E_Strawberry_Ice_Cream.set("0")
    if (var7.get() == 1):
        txtChocolate_Almond_Ice_Cream.configure(state=NORMAL)
    elif (var7.get() == 0):
        txtChocolate_Almond_Ice_Cream.configure(state=DISABLED)
        E_Chocolate_Almond_Ice_Cream.set("0")
    if (var8.get() == 1):
        txtButter_Pecan_Ice_Cream.configure(state=NORMAL)
    elif (var8.get() == 0):
        txtButter_Pecan_Ice_Cream.configure(state=DISABLED)
        E_Butter_Pecan_Ice_Cream.set("0")
    if (var9.get() == 1):
        txtChocobar_Ice_Cream.configure(state=NORMAL)
    elif (var9.get() == 0):
        txtChocobar_Ice_Cream.configure(state=DISABLED)
        E_Chocobar_Ice_Cream.set("0")
    if (var10.get() == 1):
        txtKulfi_Ice_Cream.configure(state=NORMAL)
    elif (var10.get() == 0):
        txtKulfi_Ice_Cream.configure(state=DISABLED)
        E_Kulfi_Ice_Cream.set("0")
    if (var11.get() == 1):
        txtCornato_Ice_Cream.configure(state=NORMAL)
    elif (var11.get() == 0):
        txtCornato_Ice_Cream.configure(state=DISABLED)
        E_Cornato_Ice_Cream.set("0")
    if (var12.get() == 1):
        txtFamily_Size_Ice_Cream.configure(state=NORMAL)
    elif (var12.get() == 0):
        txtFamily_Size_Ice_Cream.configure(state=DISABLED)
        E_Family_Size_Ice_Cream.set("0")
    if (var13.get() == 1):
        txtMedium_Size_Ice_Cream.configure(state=NORMAL)
    elif (var13.get() == 0):
        txtMedium_Size_Ice_Cream.configure(state=DISABLED)
        E_Medium_Size_Ice_Cream.set("0")
    if (var14.get() == 1):
        txtSmall_Size_Ice_Cream.configure(state=NORMAL)
    elif (var14.get() == 0):
        txtSmall_Size_Ice_Cream.configure(state=DISABLED)
        E_Small_Size_Ice_Cream.set("0")

        
    if (var15.get() == 1):
        txtIce_Tea.configure(state=NORMAL)
    elif (var15.get() == 0):
        txtIce_Tea.configure(state=DISABLED)
        E_Ice_Tea.set("0")
    if (var16.get() == 1):
        txtIce_Coffee.configure(state=NORMAL)
    elif (var16.get() == 0):
        txtIce_Coffee.configure(state=DISABLED)
        E_Ice_Coffee.set("0")
    if (var17.get() == 1):
        txtMineral_Water.configure(state=NORMAL)
    elif (var17.get() == 0):
        txtMineral_Water.configure(state=DISABLED)
        E_Mineral_Water.set("0")
    if (var18.get() == 1):
        txtCold_Drinks.configure(state=NORMAL)
    elif (var18.get() == 0):
        txtCold_Drinks.configure(state=DISABLED)
        E_Cold_Drinks.set("0")
    if (var19.get() == 1):
        txtTea.configure(state=NORMAL)
    elif (var19.get() == 0):
        txtTea.configure(state=DISABLED)
        E_Tea.set("0")
    if (var20.get() == 1):
        txtCoffee.configure(state=NORMAL)
    elif (var20.get() == 0):
        txtCoffee.configure(state=DISABLED)
        E_Coffee.set("0")
    if (var21.get() == 1):
        txtMilk_Packet.configure(state=NORMAL)
    elif (var21.get() == 0):
        txtMilk_Packet.configure(state=DISABLED)
        E_Milk_Packet.set("0")
    if (var22.get() == 1):
        txtYogurt_Packet.configure(state=NORMAL)
    elif (var22.get() == 0):
        txtYogurt_Packet.configure(state=DISABLED)
        E_Yogurt_Packet.set("0")
    if (var23.get() == 1):
        txtPaneer_Packet.configure(state=NORMAL)
    elif (var23.get() == 0):
        txtPaneer_Packet.configure(state=DISABLED)
        E_Paneer_Packet.set("0")
    if (var24.get() == 1):
        txtCheese_Packet.configure(state=NORMAL)
    elif (var24.get() == 0):
        txtCheese_Packet.configure(state=DISABLED)
        E_Cheese_Packet.set("0")
    if (var25.get() == 1):
        txtButter_Packet.configure(state=NORMAL)
    elif (var25.get() == 0):
        txtButter_Packet.configure(state=DISABLED)
        E_Butter_Packet.set("0")
    if (var26.get() == 1):
        txtRed_Bull.configure(state=NORMAL)
    elif (var26.get() == 0):
        txtRed_Bull.configure(state=DISABLED)
        E_Red_Bull.set("0")
    if (var27.get() == 1):
        txtGhee_Packet.configure(state=NORMAL)
    elif (var27.get() == 0):
        txtGhee_Packet.configure(state=DISABLED)
        E_Ghee_Packet.set("0")
    if (var28.get() == 1):
        txtGorkhali_Lassi.configure(state=NORMAL)
    elif (var28.get() == 0):
        txtGorkhali_Lassi.configure(state=DISABLED)
        E_Gorkhali_Lassi.set("0")

    if (var29.get() == 1):
        txtBreads.configure(state=NORMAL)
    elif (var29.get() == 0):
        txtBreads.configure(state=DISABLED)
        E_Breads.set("0")
    if (var30.get() == 1):
        txtCrackers.configure(state=NORMAL)
    elif (var30.get() == 0):
        txtCrackers.configure(state=DISABLED)
        E_Crackers.set("0")
    if (var31.get() == 1):
        txtCookies.configure(state=NORMAL)
    elif (var31.get() == 0):
        txtCookies.configure(state=DISABLED)
        E_Cookies.set("0")
    if (var32.get() == 1):
        txtBiscuits.configure(state=NORMAL)
    elif (var32.get() == 0):
        txtBiscuits.configure(state=DISABLED)
        E_Biscuits.set("0")
    if (var33.get() == 1):
        txtPastries.configure(state=NORMAL)
    elif (var33.get() == 0):
        txtPastries.configure(state=DISABLED)
        E_Pastries.set("0")
    if (var34.get() == 1):
        txtCake.configure(state=NORMAL)
    elif (var34.get() == 0):
        txtCake.configure(state=DISABLED)
        E_Cake.set("0")
    if (var35.get() == 1):
        txtDoughnuts.configure(state=NORMAL)
    elif (var35.get() == 0):
        txtDoughnuts.configure(state=DISABLED)
        E_Doughnuts.set("0")
    if (var36.get() == 1):
        txtBagels.configure(state=NORMAL)
    elif (var36.get() == 0):
        txtBagels.configure(state=DISABLED)
        E_Bagels.set("0")
    if (var37.get() == 1):
        txtBrownie.configure(state=NORMAL)
    elif (var37.get() == 0):
        txtBrownie.configure(state=DISABLED)
        E_Brownie.set("0")
    if (var38.get() == 1):
        txtPudding.configure(state=NORMAL)
    elif (var38.get() == 0):
        txtPudding.configure(state=DISABLED)
        E_Pudding.set("0")
    if (var39.get() == 1):
        txtMuffins.configure(state=NORMAL)
    elif (var39.get() == 0):
        txtMuffins.configure(state=DISABLED)
        E_Muffins.set("0")
    if (var40.get() == 1):
        txtLarge_Cone_Packet.configure(state=NORMAL)
    elif (var40.get() == 0):
        txtLarge_Cone_Packet.configure(state=DISABLED)
        E_Large_Cone_Packet.set("0")
    if (var41.get() == 1):
        txtSmall_Cone_Packet.configure(state=NORMAL)
    elif (var41.get() == 0):
        txtSmall_Cone_Packet.configure(state=DISABLED)
        E_Small_Cone_Packet.set("0")
    if (var42.get() == 1):
        txtCups_Packet.configure(state=NORMAL)
    elif (var42.get() == 0):
        txtCups_Packet.configure(state=DISABLED)
        E_Cups_Packet.set("0")


        
def Receipt_Given():
    now = datetime.datetime.now()
    new_date = now.strftime("%Y-%m-%d")
    txtReceipt.delete("1.0",END)
    x= random.randint(100,100000)
    randomRef= str(x)
    txtReceipt.insert(END,"\tManakamana Ice-Cream Stores  ")
    txtReceipt.insert(END,"\tAddress: Harmatari,Gorkha")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"\tMobile: 9856088324 \t")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"--------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    Receipt_Ref.set("BILL_No :" + randomRef)
    txtReceipt.insert(END,Receipt_Ref.get() +"\t         \t"+Date_Of_Order.strftime("%d/%m/%Y %H:%M")+"\n")
    txtReceipt.insert(END,"--------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"Customer Name :     \t\t" +Name.get()+"\n")
    txtReceipt.insert(END,"Table Number  :    \t\t" +Table_Number.get()+"\n")
    txtReceipt.insert(END,"Address  :     \t\t" +Address.get()+"\n")
    txtReceipt.insert(END,"Cashier : Sano Karki Chhetri")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    if(E_Cherry_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,'Cherry Ice-Cream\t\t\t' +E_Cherry_Ice_Cream.get() +"\n")
    if(E_Candy_Cone_Ice_Cream.get() >=str(1)):
        txtReceipt.insert(END,'Candy Cone Ice-Cream\t\t\t' +E_Candy_Cone_Ice_Cream.get() +"\n")
    if(E_Chocolate_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,'Chocolate Ice-Cream\t\t\t' +E_Chocolate_Ice_Cream.get() +"\n")
    if(E_Vanilla_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Vanilla Ice-Cream\t\t\t" +E_Vanilla_Ice_Cream.get() +"\n")
    if(E_Butter_Scotch_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Butter Scotch Ice-Cream\t\t\t" +E_Butter_Scotch_Ice_Cream.get() +"\n")
    if(E_Strawberry_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Strawberry Ice-Cream\t\t\t" +E_Strawberry_Ice_Cream.get() +"\n")

    if(E_Chocolate_Almond_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Chocolate Almond Ice-Cream\t\t\t" +E_Chocolate_Almond_Ice_Cream.get() +"\n")
    if(E_Butter_Pecan_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Butter Pecan Ice-Cream\t\t\t" +E_Butter_Pecan_Ice_Cream.get() +"\n")
    if(E_Chocobar_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Chocobar Ice-Cream\t\t\t" +E_Chocobar_Ice_Cream.get() +"\n")
    if(E_Kulfi_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Kulfi Ice-Cream\t\t\t" +E_Kulfi_Ice_Cream.get() +"\n")
    if(E_Cornato_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Cornato_Ice_Cream\t\t\t" +E_Cornato_Ice_Cream.get() +"\n")
    if(E_Family_Size_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Family Size Ice-Cream(250ml)\t\t\t" +E_Family_Size_Ice_Cream.get() +"\n")
    if(E_Medium_Size_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Medium Size Ice-Cream(160ml)\t\t\t" +E_Medium_Size_Ice_Cream.get() +"\n")
    if(E_Small_Size_Ice_Cream.get() >= str(1)):
        txtReceipt.insert(END,"Small Size Ice-Cream(80ml)\t\t\t" +E_Small_Size_Ice_Cream.get() +"\n")
    if(E_Ice_Tea.get() >= str(1)):
        txtReceipt.insert(END,"Ice Tea\t\t\t" +E_Ice_Tea.get() +"\n")
    if(E_Ice_Coffee.get() >= str(1)):
        txtReceipt.insert(END,"Ice Coffee\t\t\t" +E_Ice_Coffee.get() +"\n")
    if(E_Mineral_Water.get() >= str(1)):
        txtReceipt.insert(END,"Mineral Water\t\t\t" +E_Mineral_Water.get() +"\n")
    if(E_Cold_Drinks.get() >= str(1)):
        txtReceipt.insert(END,"Cold Drinks\t\t\t" +E_Cold_Drinks.get() +"\n")
    if(E_Tea.get() >= str(1)):
        txtReceipt.insert(END,"Tea\t\t\t" +E_Tea.get() +"\n")
    if(E_Coffee.get() >= str(1)):
        txtReceipt.insert(END,"Coffee\t\t\t" +E_Coffee.get() +"\n")
    if(E_Milk_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Milk Packet\t\t\t" +E_Milk_Packet.get() +"\n")
    if(E_Yogurt_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Yogurt Packet\t\t\t" +E_Yogurt_Packet.get() +"\n")
    if(E_Paneer_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Paneer Packet\t\t\t" +E_Paneer_Packet.get() +"\n")
    if(E_Cheese_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Cheese Packet\t\t\t" +E_Cheese_Packet.get() +"\n")
    if(E_Butter_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Butter Packet\t\t\t" +E_Butter_Packet.get() +"\n")
    if(E_Red_Bull.get() >= str(1)):
        txtReceipt.insert(END,"Red Bull\t\t\t" +E_Red_Bull.get() +"\n")
    if(E_Ghee_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Ghee Packet\t\t\t" +E_Ghee_Packet.get() +"\n")
    if(E_Gorkhali_Lassi.get() >= str(1)):
        txtReceipt.insert(END,"Gorkhali Lassi\t\t\t" +E_Gorkhali_Lassi.get() +"\n")

    if(E_Breads.get() >= str(1)):
        txtReceipt.insert(END,"Breads\t\t\t" +E_Breads.get() +"\n")
    if(E_Crackers.get() >= str(1)):
        txtReceipt.insert(END,"Crackers\t\t\t" +E_Crackers.get() +"\n")
    if(E_Cookies.get() >= str(1)):
        txtReceipt.insert(END,"Cookies\t\t\t" +E_Cookies.get() +"\n")
    if(E_Biscuits.get() >= str(1)):
        txtReceipt.insert(END,"Biscuits \t\t\t" +E_Biscuits.get() +"\n")
    if(E_Pastries.get() >= str(1)):
        txtReceipt.insert(END,"Pastries \t\t\t" +E_Pastries.get() +"\n")
    if(E_Cake.get() >= str(1)):
        txtReceipt.insert(END,"Cake \t\t\t" +E_Cake.get() +"\n")
    if(E_Doughnuts.get() >= str(1)):
        txtReceipt.insert(END,"Doughnuts\t\t\t" +E_Doughnuts.get() +"\n")
    if(E_Bagels.get() >= str(1)):
        txtReceipt.insert(END,"Bagels  \t\t\t" +E_Bagels.get() +"\n")
    if(E_Brownie.get() >= str(1)):
        txtReceipt.insert(END,"Brownie \t\t\t" +E_Brownie.get() +"\n")
    if(E_Pudding.get() >= str(1)):
        txtReceipt.insert(END,"Pudding  \t\t\t" +E_Pudding.get() +"\n")
    if(E_Muffins.get() >= str(1)):
        txtReceipt.insert(END,"Muffins  \t\t\t" +E_Muffins.get() +"\n")
    if(E_Large_Cone_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Large Cone Packet\t\t\t" +E_Large_Cone_Packet.get() +"\n")
    if(E_Small_Cone_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Small Cone Packet\t\t\t" +E_Small_Cone_Packet.get() +"\n")
    if(E_Cups_Packet.get() >= str(1)):
        txtReceipt.insert(END,"Cups Packet\t\t\t" +E_Cups_Packet.get() +"\n")
        
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"Cost of Ice-Cream        \t\t" +Cost_Of_Ice_Cream.get()+"\n")                  
    txtReceipt.insert(END,"Cost of Dairy Items        \t\t"+Cost_Of_Cold_Dairy_Product.get()+"\n")
    txtReceipt.insert(END,"Cost of Bakery Items      \t\t"+Cost_Of_Bakery_Items.get()+"\n")
    txtReceipt.insert(END,"Service Charge               \t\t"+Service_Charge.get()+"\n")
    txtReceipt.insert(END,"VAT                                   \t\t"+Vat_Paid.get() +"\n")
    txtReceipt.insert(END,"Discount                         \t\t"+Discount.get() +"\n")
    txtReceipt.insert(END,"TAX                                   \t\t"+Tax.get() +"\n")
    txtReceipt.insert(END,"Sub Total                        \t\t" +Sub_Total.get() +"\n")
    txtReceipt.insert(END,"Total Cost                       \t\t"+Total_Cost.get() +"\n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"---------------------------------------------------------------")
    txtReceipt.insert(END," \n")
    txtReceipt.insert(END,"       Thankyou For Visiting Us!!!     ")
    
    bill_no1= randomRef 
    bill_no = ('"{0}"'.format(bill_no1))
    
    c_name1= Name.get() 
    c_name = ('"{0}"'.format(c_name1))
    
    table_no1 = Table_Number.get()
    table_no = ('"{0}"'.format(table_no1))
    
    address1 = Address.get()
    address = ('"{0}"'.format(address1))
    
    date1= new_date
    date = ('"{0}"'.format(date1))
    
    total_cost1 = Total_Cost.get()
    total_cost = ('"{0}"'.format(total_cost1))
    
    insert_Update(bill_no,c_name,table_no,address,date,total_cost)
    
    
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
        Command1 = "UPDATE IceCream SET C_Name="+ str(C_Name)+"WHERE Bill_No="+str(Bill_No)
    else:
        Command1 = "INSERT INTO IceCream(Bill_No,C_Name,Table_No,Address,Date,Total_Cost) VALUES("+str(Bill_No)+","+str(C_Name)+","+str(Table_No)+","+str(Address)+","+str(Date)+","+str(Total_Cost)+")"
        
    cursor.execute(Command1)
   #for row in cursor.fetchall():
       #print (row[0])
       #print (row[3])
    database.commit()
    database.close()
    
    



def Cost_Of_Items():
    Item1=float(E_Cherry_Ice_Cream.get())
    Item2=float(E_Candy_Cone_Ice_Cream.get())
    Item3=float(E_Chocolate_Ice_Cream.get())
    Item4=float(E_Vanilla_Ice_Cream.get())
    Item5=float(E_Butter_Scotch_Ice_Cream.get())
    Item6=float(E_Strawberry_Ice_Cream.get())
    Item7=float(E_Chocolate_Almond_Ice_Cream.get())
    Item8=float(E_Butter_Pecan_Ice_Cream.get())
    Item9=float(E_Chocobar_Ice_Cream.get())
    Item10=float(E_Kulfi_Ice_Cream.get())
    Item11=float(E_Cornato_Ice_Cream.get())
    Item12=float(E_Family_Size_Ice_Cream.get())
    Item13=float(E_Medium_Size_Ice_Cream.get())
    Item14=float(E_Small_Size_Ice_Cream.get())

    Item15=float(E_Ice_Tea.get())
    Item16=float(E_Ice_Coffee.get())
    Item17=float(E_Mineral_Water.get())
    Item18=float(E_Cold_Drinks.get())
    Item19=float(E_Tea.get())
    Item20=float(E_Coffee.get())
    Item21=float(E_Milk_Packet.get())
    Item22=float(E_Yogurt_Packet.get())
    Item23=float(E_Paneer_Packet.get())
    Item24=float(E_Cheese_Packet.get())
    Item25=float(E_Butter_Packet.get())
    Item26=float(E_Red_Bull.get())
    Item27=float(E_Ghee_Packet.get())
    Item28=float(E_Gorkhali_Lassi.get())

    Item29=float(E_Breads.get())
    Item30=float(E_Crackers.get())
    Item31=float(E_Cookies.get())
    Item32=float(E_Biscuits.get())
    Item33=float(E_Pastries.get())
    Item34=float(E_Cake.get())
    Item35=float(E_Doughnuts.get())
    Item36=float(E_Bagels.get())
    Item37=float(E_Brownie.get())
    Item38=float(E_Pudding.get())
    Item39=float(E_Muffins.get())
    Item40=float(E_Large_Cone_Packet.get())
    Item41=float(E_Small_Cone_Packet.get())
    Item42=float(E_Cups_Packet.get())
    

    Price_Of_Ice_Cream = (Item1 * 80) + (Item2 * 70) +(Item3 * 75)+(Item4 * 60)+(Item5 * 65)+(Item6 * 65)+(Item7 * 85)\
                    +(Item8 * 90)+(Item9 * 70)+(Item10 * 75)+(Item11 * 80)+(Item12 * 280)+(Item13 * 180)+(Item14 * 70)
    
    Price_Of_Cold_Dairy_Product = (Item15 * 70) + (Item16 * 120) +(Item17 * 20)+(Item18 * 40)+(Item19 * 20)+(Item20 * 60)+(Item21 * 40)\
                    +(Item22 * 60)+(Item23 * 180)+(Item24 * 220)+(Item25 * 170)+(Item26 * 110)+(Item27 * 500)+(Item28 * 60)

    Price_Of_Bakery_Items = (Item29 * 60) + (Item30 * 60) +(Item31 * 70)+(Item32 * 40)+(Item33 * 80)+(Item34 * 90)+(Item35 * 60)\
                    +(Item36 * 70)+(Item37 * 80)+(Item38 * 75)+(Item39 * 90)+(Item40 * 80)+(Item41 * 60)+(Item42 * 120)
    
    MealsPrice="Rs", str('%.2f'%(Price_Of_Ice_Cream))
    DrinksPrice="Rs", str('%.2f'%(Price_Of_Cold_Dairy_Product))
    FoodsPrice="Rs", str('%.2f'%(Price_Of_Bakery_Items))
    
    Cost_Of_Ice_Cream.set(MealsPrice)
    Cost_Of_Cold_Dairy_Product.set(DrinksPrice)
    Cost_Of_Bakery_Items.set(FoodsPrice)
    
    SC="Rs", str('%.2f'%((Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items)*0.04))
    SC1=((Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items)*0.04)
    Service_Charge.set(SC)

    Tax1="Rs", str('%.2f'%((Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items + SC1)*0.05))
    Tax.set(Tax1)
    
    TT=((Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items + SC1)*0.07)

    Vat="Rs", str('%.2f'%((Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items +SC1)*0.13))
    Vat1=((Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items +SC1)*0.13)
    Vat_Paid.set(Vat)

    Sub_Total_Of_Items="Rs",str('%.2f'%(Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items + SC1+Vat1+TT))
    Sub_Total.set(Sub_Total_Of_Items)
    
    TC="Rs", str('%.2f'%(Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items + SC1+ Vat1+ TT))
    TC1=(Price_Of_Ice_Cream + Price_Of_Cold_Dairy_Product + Price_Of_Bakery_Items + SC1+Vat1+TT)
    

    Discount_Amount=TC1*0.10
    Discount_Amountt="Rs", str('%.2f'%(TC1*0.10))
    Total_Discount=TC1-Discount_Amount
    Discount.set(Discount_Amountt)

    Total_Discount1="Rs", str('%.2f'%(TC1-Discount_Amount))
    Total_Cost.set(Total_Discount1)


def qExit():
    qExit1=tkinter.messagebox.askquestion("Quit System","Do you want to quit?")
    if qExit1 == "yes":
        root.destroy()

def Reset():
    Name.set("")
    Table_Number.set("")
    Address.set("")
    Tax.set("")
    Sub_Total.set("")
    Total_Cost.set("")
    Cost_Of_Ice_Cream.set("")
    Cost_Of_Cold_Dairy_Product.set("")
    Cost_Of_Bakery_Items.set("")
    Service_Charge.set("")
    Vat_Paid.set("")
    Discount.set("")
    txtReceipt.delete("1.0",END)

    E_Cherry_Ice_Cream.set("0")
    E_Candy_Cone_Ice_Cream.set("0")
    E_Chocolate_Ice_Cream.set("0")
    E_Vanilla_Ice_Cream.set("0")
    E_Butter_Scotch_Ice_Cream.set("0")
    E_Strawberry_Ice_Cream.set("0")
    E_Chocolate_Almond_Ice_Cream.set("0")
    E_Butter_Pecan_Ice_Cream.set("0")
    E_Chocobar_Ice_Cream.set("0")
    E_Kulfi_Ice_Cream.set("0")
    E_Cornato_Ice_Cream.set("0")
    E_Family_Size_Ice_Cream.set("0")
    E_Medium_Size_Ice_Cream.set("0")
    E_Small_Size_Ice_Cream.set("0")

    E_Ice_Tea.set("0")
    E_Ice_Coffee.set("0")   
    E_Mineral_Water.set("0")
    E_Cold_Drinks.set("0")
    E_Tea.set("0")
    E_Coffee.set("0")
    E_Milk_Packet.set("0")
    E_Yogurt_Packet.set("0")
    E_Paneer_Packet.set("0")
    E_Cheese_Packet.set("0")
    E_Butter_Packet.set("0")
    E_Red_Bull.set("0")
    E_Ghee_Packet.set("0")
    E_Gorkhali_Lassi.set("0")


    E_Breads.set("0")
    E_Crackers.set("0")
    E_Cookies.set("0")
    E_Biscuits.set("0")
    E_Pastries.set("0")
    E_Cake.set("0")
    E_Doughnuts.set("0")    
    E_Bagels.set("0")
    E_Brownie.set("0")
    E_Pudding.set("0")
    E_Muffins.set("0")
    E_Large_Cone_Packet.set("0")
    E_Small_Cone_Packet.set("0")
    E_Cups_Packet.set("0")

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var40.set(0)
    var41.set(0)
    var42.set(0)

    txtCherry_Ice_Cream.configure(state=DISABLED)
    txtCandy_Cone_Ice_Cream.configure(state=DISABLED)
    txtChocolate_Ice_Cream.configure(state=DISABLED)
    txtVanilla_Ice_Cream.configure(state=DISABLED)
    txtButter_Scotch_Ice_Cream.configure(state=DISABLED)
    txtStrawberry_Ice_Cream.configure(state=DISABLED)
    txtChocolate_Almond_Ice_Cream.configure(state=DISABLED)
    txtButter_Pecan_Ice_Cream.configure(state=DISABLED)
    txtChocobar_Ice_Cream.configure(state=DISABLED)
    txtKulfi_Ice_Cream.configure(state=DISABLED)
    txtCornato_Ice_Cream.configure(state=DISABLED)
    txtFamily_Size_Ice_Cream.configure(state=DISABLED)
    txtMedium_Size_Ice_Cream.configure(state=DISABLED)
    txtSmall_Size_Ice_Cream.configure(state=DISABLED)
    txtIce_Tea.configure(state=DISABLED)
    txtIce_Coffee.configure(state=DISABLED)
    txtMineral_Water.configure(state=DISABLED)
    txtCold_Drinks.configure(state=DISABLED)
    txtTea.configure(state=DISABLED)
    txtCoffee.configure(state=DISABLED)
    txtMilk_Packet.configure(state=DISABLED)
    txtYogurt_Packet.configure(state=DISABLED)
    txtPaneer_Packet.configure(state=DISABLED)
    txtCheese_Packet.configure(state=DISABLED)
    txtButter_Packet.configure(state=DISABLED)
    txtRed_Bull.configure(state=DISABLED)
    txtGhee_Packet.configure(state=DISABLED)
    txtGorkhali_Lassi.configure(state=DISABLED)
    txtBreads.configure(state=DISABLED)
    txtCrackers.configure(state=DISABLED)
    txtCookies.configure(state=DISABLED)
    txtBiscuits.configure(state=DISABLED)
    txtPastries.configure(state=DISABLED)
    txtCake.configure(state=DISABLED)
    txtDoughnuts.configure(state=DISABLED)
    txtBagels.configure(state=DISABLED)
    txtBrownie.configure(state=DISABLED)
    txtPudding.configure(state=DISABLED)
    txtMuffins.configure(state=DISABLED)
    txtLarge_Cone_Packet.configure(state=DISABLED)
    txtSmall_Cone_Packet.configure(state=DISABLED)
    txtCups_Packet.configure(state=DISABLED)

#====================================================================================================================

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()
var41=IntVar()
var42=IntVar()


Date_Of_Order=datetime.datetime.now()
#Date_Of_Order=StringVar()
Receipt_Ref=StringVar()
Name=StringVar()
Table_Number=StringVar()
Sub_Total=StringVar()
Total_Cost=StringVar()
Cost_Of_Ice_Cream=StringVar()
Cost_Of_Cold_Dairy_Product=StringVar()
Cost_Of_Bakery_Items=StringVar()
Service_Charge=StringVar()
Vat_Paid=StringVar()
Discount=StringVar()
Tax=StringVar()
Address=StringVar()


#=====================================================================================================================


E_Cherry_Ice_Cream = StringVar()
E_Candy_Cone_Ice_Cream = StringVar()
E_Chocolate_Ice_Cream = StringVar()
E_Vanilla_Ice_Cream = StringVar()
E_Butter_Scotch_Ice_Cream = StringVar()
E_Strawberry_Ice_Cream = StringVar()
E_Chocolate_Almond_Ice_Cream = StringVar()
E_Butter_Pecan_Ice_Cream = StringVar()
E_Chocobar_Ice_Cream = StringVar()
E_Kulfi_Ice_Cream = StringVar()
E_Cornato_Ice_Cream = StringVar()
E_Family_Size_Ice_Cream = StringVar()
E_Medium_Size_Ice_Cream = StringVar()
E_Small_Size_Ice_Cream = StringVar()

E_Ice_Tea = StringVar()
E_Ice_Coffee = StringVar()
E_Mineral_Water = StringVar()
E_Cold_Drinks = StringVar()
E_Tea = StringVar()
E_Coffee = StringVar()
E_Milk_Packet = StringVar()
E_Yogurt_Packet = StringVar()
E_Paneer_Packet = StringVar()
E_Cheese_Packet = StringVar()
E_Butter_Packet = StringVar()
E_Red_Bull = StringVar()
E_Ghee_Packet = StringVar()
E_Gorkhali_Lassi = StringVar()

E_Breads = StringVar()
E_Crackers = StringVar()
E_Cookies = StringVar()
E_Biscuits = StringVar()
E_Pastries = StringVar()
E_Cake = StringVar()
E_Doughnuts = StringVar()
E_Bagels = StringVar()
E_Brownie = StringVar()
E_Pudding = StringVar()
E_Muffins = StringVar()
E_Large_Cone_Packet = StringVar()
E_Small_Cone_Packet = StringVar()
E_Cups_Packet = StringVar()






E_Cherry_Ice_Cream.set("0")
E_Candy_Cone_Ice_Cream.set("0")
E_Chocolate_Ice_Cream.set("0")
E_Vanilla_Ice_Cream.set("0")
E_Butter_Scotch_Ice_Cream.set("0")
E_Strawberry_Ice_Cream.set("0")
E_Chocolate_Almond_Ice_Cream.set("0")
E_Butter_Pecan_Ice_Cream.set("0")
E_Chocobar_Ice_Cream.set("0")
E_Kulfi_Ice_Cream.set("0")
E_Cornato_Ice_Cream.set("0")
E_Family_Size_Ice_Cream.set("0")
E_Medium_Size_Ice_Cream.set("0")
E_Small_Size_Ice_Cream.set("0")

E_Ice_Tea.set("0")
E_Ice_Coffee.set("0")
E_Mineral_Water.set("0")
E_Cold_Drinks.set("0")
E_Tea.set("0")
E_Coffee.set("0")
E_Milk_Packet.set("0")
E_Yogurt_Packet.set("0")
E_Paneer_Packet.set("0")
E_Cheese_Packet.set("0")
E_Butter_Packet.set("0")
E_Red_Bull.set("0")
E_Ghee_Packet.set("0")
E_Gorkhali_Lassi.set("0")


E_Breads.set("0")
E_Crackers.set("0")
E_Cookies.set("0")
E_Biscuits.set("0")
E_Pastries.set("0")
E_Cake.set("0")
E_Doughnuts.set("0")
E_Bagels.set("0")
E_Brownie.set("0")
E_Pudding.set("0")
E_Muffins.set("0")
E_Large_Cone_Packet.set("0")
E_Small_Cone_Packet.set("0")
E_Cups_Packet.set("0")


Date_Of_Order.strftime("%d/%m/%Y %H:%M")
#====================================================================================================================


Cherry_Ice_Cream= Checkbutton(F1aa, text="Cherry Ice-Cream", variable=var1, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Cherry_Ice_Cream.grid(row=0, column=0,sticky=W)
Candy_Cone_Ice_Cream=Checkbutton(F1aa, text="Candy Cone Ice-Cream", variable=var2, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Candy_Cone_Ice_Cream.grid(row=1, column=0,sticky=W)
Choclate_Ice_Cream=Checkbutton(F1aa, text="Choclate Ice-Cream", variable=var3, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Choclate_Ice_Cream.grid(row=2, column=0,sticky=W)
Vanilla_Ice_Cream=Checkbutton(F1aa, text="Vanilla Ice-Cream", variable=var4, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Vanilla_Ice_Cream.grid(row=3, column=0,sticky=W)
Butter_Scotch_Ice_Cream=Checkbutton(F1aa, text="Butter Scotch Ice-Cream", variable=var5, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Butter_Scotch_Ice_Cream.grid(row=4, column=0,sticky=W)
Strawberry_Ice_Cream=Checkbutton(F1aa, text="Strawberry Ice-Cream", variable=var6, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Strawberry_Ice_Cream.grid(row=5, column=0,sticky=W)
Chocolate_Almond_Ice_Cream=Checkbutton(F1aa, text="Chocolate Almond Ice-Cream", variable=var7, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Chocolate_Almond_Ice_Cream.grid(row=6, column=0,sticky=W)
Butter_Pecan_Ice_Cream=Checkbutton(F1aa, text="Butter Pecan Ice-Cream", variable=var8, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Butter_Pecan_Ice_Cream.grid(row=7, column=0,sticky=W)
Chocobar_Ice_Cream=Checkbutton(F1aa, text="Chocobar Ice-Cream", variable=var9, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Chocobar_Ice_Cream.grid(row=8, column=0,sticky=W)
Kulfi_Ice_cream=Checkbutton(F1aa, text="Kulfi Ice-Cream", variable=var10, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Kulfi_Ice_cream.grid(row=9, column=0,sticky=W)
Cornato_Ice_Cream=Checkbutton(F1aa, text="Cornato Ice-Cream", variable=var11, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Cornato_Ice_Cream.grid(row=10, column=0,sticky=W)
Family_Size_Ice_Cream=Checkbutton(F1aa, text="Family Pack (250ml)", variable=var12, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Family_Size_Ice_Cream.grid(row=11, column=0,sticky=W)
Medium_Size_Ice_Cream=Checkbutton(F1aa, text="Medium Pack (160ml)", variable=var13, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Medium_Size_Ice_Cream.grid(row=12, column=0,sticky=W)
Small_Size_Ice_Cream=Checkbutton(F1aa, text="Small Pack (80ml)", variable=var14, onvalue=1, offvalue=0, font=('arial',16,'bold'),command=chkbutton_Value)
Small_Size_Ice_Cream.grid(row=13, column=0,sticky=W)


txtCherry_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5,  textvariable=E_Cherry_Ice_Cream, justify="left", state=DISABLED)
txtCherry_Ice_Cream.grid(row=0, column=1)
txtCandy_Cone_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, textvariable=E_Candy_Cone_Ice_Cream, justify="left", state=DISABLED)
txtCandy_Cone_Ice_Cream.grid(row=1, column=1)
txtChocolate_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Chocolate_Ice_Cream)
txtChocolate_Ice_Cream.grid(row=2, column=1)
txtVanilla_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Vanilla_Ice_Cream)
txtVanilla_Ice_Cream.grid(row=3, column=1)
txtButter_Scotch_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Butter_Scotch_Ice_Cream)
txtButter_Scotch_Ice_Cream.grid(row=4, column=1)
txtStrawberry_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Strawberry_Ice_Cream)
txtStrawberry_Ice_Cream.grid(row=5, column=1)
txtChocolate_Almond_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Chocolate_Almond_Ice_Cream)
txtChocolate_Almond_Ice_Cream.grid(row=6, column=1)
txtButter_Pecan_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Butter_Pecan_Ice_Cream)
txtButter_Pecan_Ice_Cream.grid(row=7, column=1)
txtChocobar_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Chocobar_Ice_Cream)
txtChocobar_Ice_Cream.grid(row=8, column=1)
txtKulfi_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Kulfi_Ice_Cream)
txtKulfi_Ice_Cream.grid(row=9, column=1)
txtCornato_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Cornato_Ice_Cream)
txtCornato_Ice_Cream.grid(row=10, column=1)
txtFamily_Size_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Family_Size_Ice_Cream)
txtFamily_Size_Ice_Cream.grid(row=11, column=1)
txtMedium_Size_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Medium_Size_Ice_Cream)
txtMedium_Size_Ice_Cream.grid(row=12, column=1)
txtSmall_Size_Ice_Cream = Entry(F1aa, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Small_Size_Ice_Cream)
txtSmall_Size_Ice_Cream.grid(row=13, column=1)


#============================================================================================================================




Ice_Tea = Checkbutton(F1bb, text="Ice Tea  \t", variable=var15, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Ice_Tea.grid(row=0, column=0,sticky=W)
Ice_Coffee = Checkbutton(F1bb, text="Ice Coffee  \t", variable=var16, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Ice_Coffee.grid(row=1, column=0,sticky=W)
Mineral_Water = Checkbutton(F1bb, text="Mineral Water \t", variable=var17, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Mineral_Water.grid(row=2, column=0,sticky=W)
Cold_Drinks = Checkbutton(F1bb, text="Coke/Fanta/Sprite \t", variable=var18, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Cold_Drinks.grid(row=3, column=0,sticky=W)
Tea = Checkbutton(F1bb, text="Tea \t", variable=var19, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Tea.grid(row=4, column=0,sticky=W)
Coffee = Checkbutton(F1bb, text="Coffee \t", variable=var20, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Coffee.grid(row=5, column=0,sticky=W)
Milk_Packet = Checkbutton(F1bb, text="Milk \t", variable=var21, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Milk_Packet.grid(row=6, column=0,sticky=W)
Yogurt_Packet = Checkbutton(F1bb, text="Yogurt \t", variable=var22, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Yogurt_Packet.grid(row=7, column=0,sticky=W)
Paneer_Packet = Checkbutton(F1bb, text="Paneer \t", variable=var23, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Paneer_Packet.grid(row=8, column=0,sticky=W)
Cheese_Packet = Checkbutton(F1bb, text="Cheese \t", variable=var24, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Cheese_Packet.grid(row=9, column=0,sticky=W)
Butter_Packet =  Checkbutton(F1bb, text="Butter \t", variable=var25, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Butter_Packet.grid(row=10, column=0,sticky=W)
Red_Bull = Checkbutton(F1bb, text=" Red Bull \t", variable=var26, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Red_Bull.grid(row=11, column=0,sticky=W)
Ghee_Packet = Checkbutton(F1bb, text="Ghee Packet \t", variable=var27, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Ghee_Packet.grid(row=12, column=0,sticky=W)
Gorkhali_Lassi = Checkbutton(F1bb, text="Gorkhali Lassi \t", variable=var28, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Gorkhali_Lassi.grid(row=13, column=0,sticky=W)




txtIce_Tea = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Ice_Tea)
txtIce_Tea.grid(row=0, column=1)
txtIce_Coffee = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Ice_Coffee)
txtIce_Coffee.grid(row=1, column=1)
txtMineral_Water = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Mineral_Water)
txtMineral_Water.grid(row=2, column=1)
txtCold_Drinks = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Cold_Drinks)
txtCold_Drinks.grid(row=3, column=1)
txtTea = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Tea)
txtTea.grid(row=4, column=1)
txtCoffee = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Coffee)
txtCoffee.grid(row=5, column=1)
txtMilk_Packet =Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Milk_Packet)
txtMilk_Packet.grid(row=6, column=1)
txtYogurt_Packet = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Yogurt_Packet)
txtYogurt_Packet.grid(row=7, column=1)
txtPaneer_Packet = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Paneer_Packet)
txtPaneer_Packet.grid(row=8, column=1)
txtCheese_Packet = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Cheese_Packet)
txtCheese_Packet.grid(row=9, column=1)
txtButter_Packet = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Butter_Packet)
txtButter_Packet.grid(row=10, column=1)
txtRed_Bull = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Red_Bull)
txtRed_Bull.grid(row=11, column=1)
txtGhee_Packet = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Ghee_Packet)
txtGhee_Packet.grid(row=12, column=1)
txtGorkhali_Lassi = Entry(F1bb, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Gorkhali_Lassi)
txtGorkhali_Lassi.grid(row=13, column=1)

#=====================================================================================================================


Breads = Checkbutton(F1cc, text="Breads\t", variable=var29, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Breads.grid(row=0, column=0,sticky=W)
Crackers = Checkbutton(F1cc, text="Crackers\t", variable=var30, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Crackers.grid(row=1, column=0,sticky=W)
Cookies = Checkbutton(F1cc, text="Cookies\t", variable=var31, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Cookies.grid(row=2, column=0,sticky=W)
Biscuits = Checkbutton(F1cc, text="Biscuits\t", variable=var32, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Biscuits.grid(row=3, column=0,sticky=W)
Pastries = Checkbutton(F1cc, text="Pastries\t", variable=var33, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Pastries.grid(row=4, column=0,sticky=W)
Cake= Checkbutton(F1cc, text="Cake\t", variable=var34, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Cake.grid(row=5, column=0,sticky=W)
Doughnuts = Checkbutton(F1cc, text="Doughnuts\t", variable=var35, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Doughnuts.grid(row=6, column=0,sticky=W)
Bagels = Checkbutton(F1cc, text="Bagels\t", variable=var36, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Bagels.grid(row=7, column=0,sticky=W)
Brownie = Checkbutton(F1cc, text="Brownie\t", variable=var37, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Brownie.grid(row=8, column=0,sticky=W)
Pudding = Checkbutton(F1cc, text="Pudding\t", variable=var38, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Pudding.grid(row=9, column=0,sticky=W)
Muffins = Checkbutton(F1cc, text="Muffins\t", variable=var39, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Muffins.grid(row=10, column=0,sticky=W) 
Large_Cone_Packet = Checkbutton(F1cc, text="Large Cone Packet   ", variable=var40, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Large_Cone_Packet.grid(row=11, column=0,sticky=W)
Small_Cone_Packet = Checkbutton(F1cc, text="Small Cone Packet   ", variable=var41, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Small_Cone_Packet.grid(row=12, column=0,sticky=W)
Cups_Packet = Checkbutton(F1cc, text="Cups Packet    ", variable=var42, onvalue=1, offvalue=0, font=('arial',16,'bold'), command=chkbutton_Value)
Cups_Packet.grid(row=13, column=0,sticky=W)


txtBreads = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5,  textvariable=E_Breads, justify="left", state=DISABLED)
txtBreads.grid(row=0, column=1)
txtCrackers = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, textvariable=E_Crackers, justify="left", state=DISABLED)
txtCrackers.grid(row=1, column=1)
txtCookies = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Cookies)
txtCookies.grid(row=2, column=1)
txtBiscuits = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Biscuits)
txtBiscuits.grid(row=3, column=1)
txtPastries = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Pastries)
txtPastries.grid(row=4, column=1)
txtCake = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Cake)
txtCake.grid(row=5, column=1)
txtDoughnuts = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Doughnuts)
txtDoughnuts.grid(row=6, column=1)
txtBagels = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Bagels )
txtBagels.grid(row=7, column=1)
txtBrownie = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Brownie)
txtBrownie.grid(row=8, column=1)
txtPudding = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Pudding)
txtPudding.grid(row=9, column=1)
txtMuffins = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Muffins)
txtMuffins.grid(row=10, column=1)
txtLarge_Cone_Packet = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Large_Cone_Packet)
txtLarge_Cone_Packet.grid(row=11, column=1)
txtSmall_Cone_Packet = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Small_Cone_Packet)
txtSmall_Cone_Packet.grid(row=12, column=1)
txtCups_Packet = Entry(F1cc, font=('arial',16,'bold'), bd=4, width=5, justify="left", state=DISABLED, textvariable=E_Cups_Packet)
txtCups_Packet.grid(row=13, column=1)


#=====================================================================================================================

lblReceipt = Label(F2a,font=('arial',12,'bold'), text="Receipt:",bd=2,anchor='w')
lblReceipt.grid(row=0, column=0 ,sticky=W)
txtReceipt =Text(F2a, font=('arial',12,'bold'), bd=2, width=35,height=31,bg="powder blue" )
txtReceipt.grid(row=1, column=0)

lblName=Label(F2aa, font=('arial',12,'bold'),text="   Name       ",bd=5,anchor='w')
lblName.grid(row=0,column=0,sticky=W)
txtName=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Name,insertwidth=2)
txtName.grid(row=0,column=1,sticky=W)

lblTable_Number=Label(F2aa, font=('arial',12,'bold'),text="  Table Number       ",bd=5,anchor='w')
lblTable_Number.grid(row=1,column=0,sticky=W)
txtTable_Number=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Table_Number,insertwidth=2)
txtTable_Number.grid(row=1,column=1,sticky=W)

lblAddress=Label(F2aa, font=('arial',12,'bold'),text="   Address       ",bd=5,anchor='w')
lblAddress.grid(row=2,column=0,sticky=W)
txtAddress=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Address,insertwidth=2)
txtAddress.grid(row=2,column=1,sticky=W)

lblTax=Label(F2aa, font=('arial',12,'bold'),text="   Tax       ",bd=5,anchor='w')
lblTax.grid(row=3,column=0,sticky=W)
txtTax=Entry(F2aa, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Tax,insertwidth=2)
txtTax.grid(row=3,column=1,sticky=W)


lblCost_Of_Ice_Cream=Label(F2bb, font=('arial',12,'bold'),text="Cost of Ice-Cream",bd=5, anchor='w')
lblCost_Of_Ice_Cream.grid(row=0,column=0,sticky=W)
txtCost_Of_Ice_Cream=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Ice_Cream, insertwidth=2)
txtCost_Of_Ice_Cream.grid(row=0,column=1,sticky=W)

lblCost_Of_Cold_Dairy_Product=Label(F2bb, font=('arial',12,'bold'),text="Cost of Dairy Items ",bd=4,anchor='w')
lblCost_Of_Cold_Dairy_Product.grid(row=1, column=0, sticky=W)
txtCost_Of_Cold_Dairy_Product=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Cost_Of_Cold_Dairy_Product, insertwidth=2)
txtCost_Of_Cold_Dairy_Product.grid(row=1, column=1, sticky=W)

lblCost_Of_Bakery_Items=Label(F2bb, font=('arial',12,'bold'),text="Cost of Bakery Items ",bd=4,anchor='w')
lblCost_Of_Bakery_Items.grid(row=2,column=0,sticky=W)
txtCost_Of_Bakery_Items=Entry(F2bb, font=('arial', 12, 'bold'), bd=5, justify="left", textvariable=Cost_Of_Bakery_Items, insertwidth=2)
txtCost_Of_Bakery_Items.grid(row=2, column=1, sticky=W)

lblService_Charge=Label(F2bb, font=('arial',12,'bold'),text="Service Charge    ", bd=5,anchor='w')
lblService_Charge.grid(row=3,column=0,sticky=W)
txtService_Charge=Entry(F2bb, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Service_Charge, insertwidth=2)
txtService_Charge.grid(row=3,column=1,sticky=W)



lblVat_Paid=Label(F2cc, font=('arial',12,'bold'), text="   Vat Paid    ", bd=5, anchor='w')
lblVat_Paid.grid(row=0, column=0, sticky=W)
txtVat_Paid=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Vat_Paid, insertwidth=2)
txtVat_Paid.grid(row=0,column=1,sticky=W)

lblDiscount=Label(F2cc, font=('arial',12,'bold'), text="   Discount       ",bd=5, anchor='w')
lblDiscount.grid(row=1, column=0, sticky=W)
txtDiscount=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Discount, insertwidth=2)
txtDiscount.grid(row=1, column=1, sticky=W)

lblSub_Total=Label(F2cc, font=('arial',12,'bold'), text="   Sub Total     ",bd=5, anchor='w')
lblSub_Total.grid(row=2,column=0,sticky=W)
txtSub_Total=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left",textvariable=Sub_Total, insertwidth=2)
txtSub_Total.grid(row=2,column=1,sticky=W)

lblTotal_Cost=Label(F2cc, font=('arial',12,'bold'), text="   Total Cost    ",bd=5, anchor='w')
lblTotal_Cost.grid(row=3,column=0,sticky=W)
txtTotal_Cost=Entry(F2cc, font=('arial',12,'bold'), bd=5, justify="left", textvariable=Total_Cost, insertwidth=2)
txtTotal_Cost.grid(row=3, column=1, sticky=W)

#========================================================================================================================
btnTotal_Cost=Button(F2b,padx=16,pady=1,bd=3,bg="red",font=('arial',12,'bold'),width=4,text="  Total  ",command=Cost_Of_Items)
btnTotal_Cost.grid(row=0,column=0)

btnReceipt=Button(F2b,padx=16,pady=1,bd=3,bg="blue",font=('arial',12,'bold'),width=4,text="  Receipt   ",command=Receipt_Given)
btnReceipt.grid(row=0,column=1)

btnReset=Button(F2b,padx=16,pady=1,bd=3,bg="yellow",font=('arial',12,'bold'),width=4,text="  Reset   ",command=Reset)
btnReset.grid(row=0,column=2)

btnExit=Button(F2b,padx=16,pady=1,bd=3,bg="green",font=('arial',12,'bold'),width=4,text="  Exit ",command=qExit)
btnExit.grid(row=0,column=3)

#=============================================================================================================================
class Application(Frame):
   
    def __init__(self, master):
        
        Frame.__init__(self, master)
        self.entry = Entry(master, width=28, font=("Arial",25,"bold"),justify=RIGHT)
        self.entry.grid(row=0, column=0, columnspan=6, sticky="w",padx=45, pady = 45)
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()
        
        
    def add_chr(self, char, btn=None):
    
        self.entry.configure(state="normal")
        self.flash(btn) # Flash a button correspond to keystroke
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0,END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def backspace(self):
        
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            # Clears full entry when "Invalid Input"
            text = self.entry.get()[:-1]
            self.entry.delete(0,END)
            self.entry.insert(0,text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):

        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def factorial(self):

        self.entry.configure(state="normal")
        num=float(self.entry.get())
        y=math.factorial(num)
        self.entry.delete(0,END)
        self.entry.insert(0,y)

        self.entry.configure(state="disabled")

    def Sin_value(self):

        self.entry.configure(state="normal")
        sin=float(self.entry.get())
        angle=(sin*2*math.pi)/360.0
        a=math.sin(angle)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")


    def Cos_value(self):

        self.entry.configure(state="normal")
        cos=float(self.entry.get())
        angle=(cos*2*math.pi)/360.0
        a=math.cos(angle)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")

    def Tan_value(self):

        self.entry.configure(state="normal")
        tan=float(self.entry.get())
        angle=(tan*2*math.pi)/360.0
        a=math.tan(angle)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")


    def Log_value(self):
        
        self.entry.configure(state="normal")
        log1=float(self.entry.get())
        a=math.log(log1,10)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")

    def Ln_value(self):
        
        self.entry.configure(state="normal")
        ln1=float(self.entry.get())
        a=math.log(ln1)
        self.entry.delete(0,END)
        self.entry.insert(0,a)
        self.entry.configure(state="disabled")

    def Cube_Root(self):
        self.entry.configure(state="normal")
        cube=float(self.entry.get())
        z=math.pow(cube,1/3)
        self.entry.delete(0,END)
        self.entry.insert(0,z)
        self.entry.configure(state="disabled")

    def Inverse(self):
        self.entry.configure(state="normal")
        inverse=float(self.entry.get())
        x=1/inverse
        self.entry.delete(0,END)
        self.entry.insert(0,x)
        self.entry.configure(state="disabled")
        
        
    def qExit(self):
        self.qExit1=tkinter.messagebox.askquestion("Quit System","Do you want to quit?")
        if self.qExit1 == "yes":
            root.destroy()

    def calculate(self):
        
        self.entry.configure(state="normal")
        e = self.entry.get()
        e = e.replace("√","sqr")
        e = e.replace("×", "*")
        e = e.replace("²", "**2")
        e = e.replace("^", "**")
        e = e.replace("÷", "/")
        e = e.replace("^3", "**3")
        e = e.replace("e","*2.7182818285")
        e = e.replace("π","*3.1415926536")
    

        try:
            ans = eval(e)
        except Exception as ex:
            self.entry.delete(0,END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0,END)
            if len(str(ans)) > 20: # Alleviates problem of large numbers
                self.entry.insert(0, '{:.10e}'.format(ans))
            else:
                self.entry.insert(0, ans)
        self.entry.configure(state="disabled")

    def flash(self,btn):

        if btn != None:
            btn.config(bg="yellow")
            if btn == self.c_bttn:
                self.backspace()
                self.master.after(100, lambda: btn.config(bg="blue"))
            elif btn == self.eq_bttn:
                self.master.after(100, lambda: btn.config(bg="blue"))
                self.calculate()
            elif btn == self.ac_bttn:
                self.clear_all()
                self.master.after(100, lambda: btn.config(bg="blue"))
            else:
                self.master.after(100, lambda: btn.config(bg="blue"))
        else:
            pass

    def bind_buttons(self, master):
        
        master.bind("<Return>", lambda event, btn=self.eq_bttn: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_bttn: self.flash(btn))
        master.bind("9", lambda event, char="9", btn=self.nine_bttn: self.add_chr(char, btn))
        master.bind("8", lambda event, char="8", btn=self.eight_bttn: self.add_chr(char, btn))
        master.bind("7", lambda event, char="7", btn=self.seven_bttn: self.add_chr(char, btn))
        master.bind("6", lambda event, char="6", btn=self.six_bttn: self.add_chr(char, btn))
        master.bind("5", lambda event, char="5", btn=self.five_bttn: self.add_chr(char, btn))
        master.bind("4", lambda event, char="4", btn=self.four_bttn: self.add_chr(char, btn))
        master.bind("3", lambda event, char="3", btn=self.three_bttn: self.add_chr(char, btn))
        master.bind("2", lambda event, char="2", btn=self.two_bttn: self.add_chr(char, btn))
        master.bind("1", lambda event, char="1", btn=self.one_bttn: self.add_chr(char, btn))
        master.bind("0", lambda event, char="0", btn=self.zero_bttn: self.add_chr(char, btn))
        master.bind("*", lambda event, char="×", btn=self.mult_bttn: self.add_chr(char, btn))
        master.bind("/", lambda event, char="÷", btn=self.div_bttn: self.add_chr(char, btn))
        master.bind("^", lambda event, char="^", btn=self.sqr_bttn: self.add_chr(char, btn))
        master.bind("%", lambda event, char="%", btn=self.mod_bttn: self.add_chr(char, btn))
        master.bind(".", lambda event, char=".", btn=self.dec_bttn: self.add_chr(char, btn))
        master.bind("-", lambda event, char="-", btn=self.sub_bttn: self.add_chr(char, btn))
        master.bind("+", lambda event, char="+", btn=self.add_bttn: self.add_chr(char, btn))
        master.bind("(", lambda event, char="(", btn=self.lpar_bttn: self.add_chr(char, btn))
        master.bind(")", lambda event, char=")", btn=self.rpar_bttn: self.add_chr(char, btn))
        master.bind("AC",lambda event, char="AC",btn=self.ac_bttn: self.flash(btn), self.clear_all)
        master.bind("Log",lambda event, char="Log", btn=self.Log_bttn: self.add_chr(char, btn))
        master.bind("Ln", lambda event, char="Ln", btn=self.Ln_bttn: self.add_chr(char, btn))
        master.bind("Pi", lambda event, char="Pi", btn=self.Pi_bttn: self.add_chr(char, btn))
        master.bind("Exp", lambda event, char="Exp", btn=self.Exp_bttn: self.add_chr(char, btn))
        master.bind("^3", lambda event, char="^3", btn=self.Cube_bttn: self.add_chr(char, btn))
        
        
    def create_widgets(self):

        self.seven_bttn = Button(self, text="7", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.seven_bttn["command"]=lambda: self.add_chr(7)
        self.seven_bttn.grid(row=2, column=0)

        self.eight_bttn = Button(self, text="8", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.eight_bttn["command"]=lambda: self.add_chr(8)
        self.eight_bttn.grid(row=2, column=1)

        self.nine_bttn = Button(self, text="9", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.nine_bttn["command"]=lambda: self.add_chr(9)
        self.nine_bttn.grid(row=2, column=2)

        self.ac_bttn = Button(self, text='AC', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.ac_bttn["command"]=lambda: self.clear_all()
        self.ac_bttn.grid(row=2, column=3)

        self.c_bttn = Button(self, text='←', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.c_bttn["command"]=lambda: self.backspace()
        self.c_bttn.grid(row=2, column=4 )

        self.Off_bttn = Button(self, text='OFF', width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Off_bttn["command"]=lambda: self.qExit()
        self.Off_bttn.grid(row=2, column=5 )

        self.four_bttn = Button(self, text="4", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.four_bttn["command"]=lambda: self.add_chr(4)
        self.four_bttn.grid(row=3, column=0)

        self.five_bttn = Button(self, text="5", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.five_bttn["command"]=lambda: self.add_chr(5)
        self.five_bttn.grid(row=3, column=1)

        self.six_bttn = Button(self, text="6", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.six_bttn["command"]=lambda: self.add_chr(6)
        self.six_bttn.grid(row=3, column=2)

        self.div_bttn = Button(self, text="÷", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.div_bttn["command"]=lambda: self.add_chr('/')
        self.div_bttn.grid(row=3, column=3)

        self.lpar_bttn = Button(self, text="(", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.lpar_bttn["command"]=lambda: self.add_chr('(')
        self.lpar_bttn.grid(row=3, column=4)

        self.rpar_bttn = Button(self, text=")", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.rpar_bttn["command"]=lambda: self.add_chr(')')
        self.rpar_bttn.grid(row=3, column=5)

        self.one_bttn = Button(self, text="1", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.one_bttn["command"]=lambda: self.add_chr(1)
        self.one_bttn.grid(row=4, column=0)

        self.two_bttn = Button(self, text="2", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.two_bttn["command"]=lambda: self.add_chr(2)
        self.two_bttn.grid(row=4, column=1)

        self.three_bttn = Button(self, text="3", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.three_bttn["command"]=lambda: self.add_chr(3)
        self.three_bttn.grid(row=4, column=2)

        self.sub_bttn = Button(self, text="-", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.sub_bttn["command"]=lambda: self.add_chr('-')
        self.sub_bttn.grid(row=4, column=3)

        self.mult_bttn = Button(self, text="×", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.mult_bttn["command"]=lambda: self.add_chr('×')
        self.mult_bttn.grid(row=4, column=4)

        self.sqr_bttn = Button(self, text="^", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.sqr_bttn["command"]=lambda: self.add_chr('^')
        self.sqr_bttn.grid(row=4, column=5)

        self.dec_bttn = Button(self, text=".", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.dec_bttn["command"]=lambda: self.add_chr('.')
        self.dec_bttn.grid(row=5, column=0)

        self.zero_bttn = Button(self, text="0", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.zero_bttn["command"]=lambda: self.add_chr(0)
        self.zero_bttn.grid(row=5, column=1)

        self.add_bttn = Button(self, text="+", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.add_bttn["command"]=lambda: self.add_chr('+')
        self.add_bttn.grid(row=5, column=2)

        self.mod_bttn = Button(self, text="%", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.mod_bttn["command"]=lambda: self.add_chr('%')
        self.mod_bttn.grid(row=5, column=3)

        self.sq_bttn = Button(self, text="√x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.sq_bttn["command"]=lambda: self.add_chr('√(')
        self.sq_bttn.grid(row=5, column=4)

        self.root_Cube_bttn = Button(self, text=" ³√x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.root_Cube_bttn["command"]=lambda: self.Cube_Root()
        self.root_Cube_bttn.grid(row=5, column=5)

        self.Log_bttn = Button(self, text="Log", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Log_bttn["command"]=lambda: self.Log_value()
        self.Log_bttn.grid(row=6, column=0)

        self.Ln_bttn = Button(self, text="ln", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Ln_bttn["command"]=lambda: self.Ln_value()
        self.Ln_bttn.grid(row=6, column=1)

        self.Inverse_bttn = Button(self, text="1/x", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Inverse_bttn["command"]=lambda: self.Inverse()
        self.Inverse_bttn.grid(row=6, column=2)

        self.Pi_bttn = Button(self, text="π", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Pi_bttn["command"]=lambda: self.add_chr('π')
        self.Pi_bttn.grid(row=6, column=3)

        self.Exp_bttn = Button(self, text="Exp", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Exp_bttn["command"]=lambda: self.add_chr('e')
        self.Exp_bttn.grid(row=6, column=4)

        self.Cube_bttn = Button(self, text="x^3", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Cube_bttn["command"]=lambda: self.add_chr('^3')
        self.Cube_bttn.grid(row=6, column=5)

        self.Sin_bttn = Button(self, text="Sin", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Sin_bttn["command"]=lambda: self.Sin_value()
        self.Sin_bttn.grid(row=7, column=0)

        self.Cos_bttn = Button(self, text="Cos", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Cos_bttn["command"]=lambda: self.Cos_value()
        self.Cos_bttn.grid(row=7, column=1)

        self.Tan_bttn = Button(self, text="Tan", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Tan_bttn["command"]=lambda: self.Tan_value()
        self.Tan_bttn.grid(row=7, column=2)

        self.Factorial_bttn = Button(self, text="!", width=9, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.Factorial_bttn["command"]=lambda: self.factorial()
        self.Factorial_bttn.grid(row=7, column=3)
        
        self.eq_bttn = Button(self, text="=", width=20, height=3,padx=6, pady=6,bd=2,fg="blue",font=("arial",12,"bold"),bg="black")
        self.eq_bttn["command"]=lambda: self.calculate()
        self.eq_bttn.grid(row=7, column=4, columnspan=2)



        

root = Tk()
root.geometry()
app = Application(root)
root.mainloop()



root.mainloop()


