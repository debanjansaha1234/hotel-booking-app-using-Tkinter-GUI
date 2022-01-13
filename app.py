from tkinter import *
import os
import mysql.connector as sq
import tkinter as tk
import tkinter.messagebox
def booking():
    global screen13
    screen13=Toplevel(screen)
    screen13.geometry("800x710")
    screen13.title("boking page")
    screen13.iconbitmap(r'icon_gtp_icon.ico')
    photo5=PhotoImage(file="oberoi-udaivilas-udaipur.png")
    cv5=tk.Canvas(screen13)
    cv5.pack(side='right', fill='both', expand='yes')
    label4=Label(cv5,image=photo5)
    label4.image=photo5
    label4.pack()
    
    global name4
    global name_entry2
    global room1
    global room_entry2
    global room2
    global room_entry1
    global checkin5
    global check_entry1
    global checkout60
    global check_out_entry5
    global rooms
    global no_entry
    global bud_entry
    global budget
    global dur_entry
    global duration
    
    name4=StringVar()
    room1=StringVar()
    room2=StringVar()
    checkin5=StringVar()
    checkout60=StringVar()
    rooms=IntVar()
    budget=IntVar()
    duration=IntVar()
    
    Label(screen13,text=" ENTER YOUR  FULL NAME(IN CAPS)",font=("calibri",15,("bold "))).place(x=30,y=30)
    name_entry2=Entry(screen13,textvariable=name4,font=("calibri",15,("bold ")))
    name_entry2.place(x=560,y=30)
    
    Label(screen13,text=" ENTER YOUR ROOM CLASS(EXECUTIVE/LUXURY) (IN CAPS) ",font=("calibri",15,("bold "))).place(x=30,y=100)
    room_entry2=Entry(screen13,textvariable=room1,font=("calibri",15,("bold ")))
    room_entry2.place(x=560,y=100)
    
    Label(screen13,text=" ENTER YOUR ROOM TYPE (AC/NON-AC) (IN CAPS)",font=("calibri",15,("bold "))).place(x=30,y=170)
    room_entry1=Entry(screen13,textvariable=room2,font=("calibri",15,("bold ")))
    room_entry1.place(x=560,y=170)
    
   
    Label(screen13,text=" ENTER YOUR CHECK IN DATE (YYYY-MM-DD)",font=("calibri",15,("bold "))).place(x=30,y=240)
    check_entry1=Entry(screen13,textvariable=checkin5,font=("calibri",15,("bold ")))
    check_entry1.place(x=560,y=240)
 
    Label(screen13,text="ENTER YOUR CHECK OUT DATE(YYYY-MM-DD)",font=("calibri",15,("bold "))).place(x=30,y=310)
    check_out_entry5=Entry(screen13,textvariable=checkout60,font=("calibri",15,("bold ")))
    check_out_entry5.place(x=560,y=310)
    
    Label(screen13,text=" ENTER NO OF ROOMS",font=("calibri",15,("bold "))).place(x=30,y=380)
    no_entry=Entry(screen13,textvariable=rooms,font=("calibri",15,("bold ")))
    no_entry.place(x=560,y=380)
   
    Label(screen13,text="ENTER YOUR BUDGET",font=("calibri",15,("bold "))).place(x=30,y=450)
    bud_entry=Entry(screen13,textvariable=budget,font=("calibri",15,("bold ")))
    bud_entry.place(x=560,y=450)
    
    Label(screen13,text="ENTER YOUR DURATION",font=("calibri",15,("bold "))).place(x=30,y=520)
    dur_entry=Entry(screen13,textvariable=duration,font=("calibri",15,("bold ")))
    dur_entry.place(x=560,y=520)
    
    Button(screen13,text="Check Your Preffered Room",bg="green",font=("calibri",15,("bold ")),relief=GROOVE,command=preference).place(x=300,y=590) 
    Button(screen13,text="Generate Bill",bg="red",font=("calibri",15,("bold ")),relief=GROOVE,command=payment).place(x=360,y=645) 
    Label(screen13,text="*NOTE- Luxury class doesn not have non-ac type of room ",fg="red",font=("calibri",10,("bold "))).place(x=250,y=690)
def payment():
    global name_1
    global room_1
    global room_2
    global check3_u
    global checkyo
    global rooms_1
    name_1=name4.get()
    room_1=room1.get()
    room_2=room2.get()
    check3_u=checkin5.get()
    checkyo=checkout60.get()
    rooms_1=rooms.get()
    if checkyo<check3_u:
        tkinter.messagebox.showerror("error","Invalid date")
    else:
         paymentr()

def preference():
    global root2
    root2=Toplevel()
    root2.title("Preffered")
    root2.geometry("430x150")
    root2.iconbitmap(r'icon_gtp_icon.ico')
    root2.configure(background="white")
    bud1=budget.get()
    dur1=duration.get()
    ans=bud1/dur1
    if ans>=10000:
        Label(root2,bg="white",text="BASED ON YOUR GIVEN BUDGET AND DURATION ",font=("calibri",15,("bold "))).pack()
        Label(root2,bg="white",text=" WE SUGGEST YOU  ",font=("calibri",15,("bold "))).pack()

        Label(root2,bg="white",text=" ROOM TYPE= AC , ROOM CLASS=LUXURY",font=("calibri",15,("bold "))).pack()
        
    elif ans<10000 and ans>=5000:
        Label(root2,bg="white",text="BASED ON YOUR GIVEN BUDGET AND DURATION ",font=("calibri",15,("bold "))).pack()
        Label(root2,bg="white",text=" WE SUGGEST YOU  ",font=("calibri",15,("bold "))).pack()

        Label(root2,bg="white",text=" ROOM TYPE= AC , ROOM CLASS=EXECUTIVE",font=("calibri",15,("bold "))).pack()
    elif ans<5000 and ans>=3000:
        Label(root2,bg="white",text="BASED ON YOUR GIVEN BUDGET AND DURATION ",font=("calibri",15,("bold "))).pack()
        Label(root2,bg="white",text=" WE SUGGEST YOU  ",font=("calibri",15,("bold "))).pack()
        Label(root2,bg="white",text=" ROOM TYPE=  NON AC , ROOM CLASS=EXECUTIVE",font=("calibri",15,("bold "))).pack()
    else:
        Label(root2,bg="white",text="THIS BUDGET IS VERY LOW ",font=("calibri",15,("bold "))).pack()
    Label(root2,bg="white",text="").pack()
    Button(root2,text="OK",font=("calibri",15,("bold ")),relief=GROOVE,command=des1).pack()
    
def des1():
    root2.destroy()
def paymentr():
    global screen14
    screen14=Toplevel()
    screen14.geometry("342x350")
    screen14.iconbitmap(r'icon3_T88_icon.ico')
    screen14.title("payement page")
    cv6=tk.Canvas(screen14)
    cv6.pack(side='right', fill='both', expand='yes')
    photo6=PhotoImage(file="pay.png")
    label5=Label(cv6,image=photo6)
    label5.image=photo6
    label5.pack()
    
    Label(screen14,text="Select Your  Bank and Debit Card",bg="white",font=("Calibri",13,("bold"))).place(x=60,y=10)
    Button(screen14,text="State Bank Of India- MasterCard",bg="yellow",font=("Calibri",13,("bold")),relief=GROOVE,command=payment1).place(x=20,y=50)
    ph=PhotoImage(file="IMG_20190815_184954.png")
    
    la=Label(screen14,image=ph)
    la.image=ph
    la.place(x=280,y=50)
    
    Button(screen14,text="BOI- MasterCard",bg="red",font=("Calibri",13,("bold")),relief=GROOVE,command=payment2).place(x=95,y=110)
    ph1=PhotoImage(file="IMG_20190815_184954.png")
    lab=Label(screen14,image=ph1)
    lab.image=ph1
    lab.place(x=280,y=110)
    Button(screen14,text="Corporation Bank- RuPay",bg="blue",font=("Calibri",13,("bold")),relief=GROOVE,command=payment3).place(x=40,y=180)
    ph2=PhotoImage(file="rupay.png")
    labe=Label(screen14,image=ph2)
    labe.image=ph2
    labe.place(x=270,y=180)
    
    Button(screen14,text="HDFC- RuPay",bg="pink",font=("Calibri",13,("bold")),relief=GROOVE,command=payment4).place(x=100,y=250)
    ph3=PhotoImage(file="rupay.png")
    labe1=Label(screen14,image=ph3)
    labe1.image=ph3
    labe1.place(x=270,y=250)

def payment4():
    global screen15
    screen15=Toplevel()
    screen15.geometry("700x700")
    screen15.iconbitmap(r'bill_n4I_icon.ico')

    screen15.title("payement page")
    screen15.configure(background="white")
    global room_1
    global room_2
    global name_1
    global check3_u
    global checkyo
    global rooms_1
    
    global price3
    name_1=name4.get()
    room_1=room1.get()
    room_2=room2.get()
    check3_u=checkin5.get()
    checkyo=checkout60.get()
    rooms_1=rooms.get()
    Label(screen15,bg="white",text="BILL",font=("calibri",20,("underline bold")),fg="magenta").grid(row=1,column=2)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="NAME",font=("calibri",14,("underline bold"))).grid(row=4,column=1)
    
    Label(screen15,bg="white",text=name_1,font=("calibri",14,("underline bold"))).grid(row=4,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="ROOM CLASS",font=("calibri",14,("underline bold"))).grid(row=15,column=1)
    Label(screen15,bg="white",text=room_1,font=("calibri",14,("underline bold"))).grid(row=15,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
   
    
    Label(screen15,bg="white",text="ROOM TYPE",font=("calibri",14,("underline bold"))).grid(row=24,column=1)
    Label(screen15,bg="white",text=room_2,font=("calibri",14,("underline bold"))).grid(row=24,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK IN DATE",font=("calibri",14,("underline bold"))).grid(row=33,column=1)
    Label(screen15,bg="white",text=check3_u,font=("calibri",14,("underline bold"))).grid(row=33,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK OUT DATE",font=("calibri",14,("underline bold"))).grid(row=42,column=1)
    Label(screen15,bg="white",text=checkyo,font=("calibri",14,("underline bold"))).grid(row=42,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="NO OF ROOMS BOOKED",font=("calibri",14,("underline bold"))).grid(row=51,column=1)
    Label(screen15,bg="white",text=rooms_1,font=("calibri",14,("underline bold"))).grid(row=51,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
  
    Label(screen15,bg="white",text="PRICE",font=("calibri",14,("underline bold"))).grid(row=60,column=1)
    price3=IntVar()
    
    if room_1== "LUXURY" and room_2=="AC":
        price3=rooms_1*10000
    elif room_1=='EXECUTIVE' and room_2=='AC':
        price3=rooms_1*5000
    elif room_1=='EXECUTIVE' and room_2=='NON AC':
        price3=rooms_1*3000
    Label(screen15,bg="white",text=price3,font=("calibri",14,("underline bold"))).grid(row=60,column=3)
    Label(screen15,bg="white",text="").grid()
        

    Label(screen15,bg="white",text="Payment through HDFC-Rupay ",font=("calibri",18,("underline bold"))).grid(row=79,column=2)
    Label(screen15,bg="white",text="*Note please take screenshot of the bill for future reference  ",fg="red").grid(row=80,column=2)
    Label(screen15,bg="white",text="").grid()
    Button(screen15,text="Pay",font=("calibri",12,("underline bold")),relief=GROOVE,command=add_new_user3).grid(row=90,column=2)
    



def add_new_user3():
    global screen16
    screen16=Toplevel()
    screen16.geometry("550x245")
    cv7=tk.Canvas(screen16)
    screen16.title("payment")
    screen16.iconbitmap(r'icon2_emk_icon.ico')
    cv7.pack(side='right', fill='both', expand='yes')
    photo7=PhotoImage(file="epay.png")
    label7=Label(cv7,image=photo7)
    label7.image=photo7
    label7.pack()

   
    global card_entry
    global card1_entry
    global debit_entry
    global debit
    global card
    global cvv
    debit=IntVar()
    cvv=IntVar()
    card=IntVar()
    Label(screen16,bg="white",text="ENTER YOUR DEBIT CARD NUMBER ",font=("calibri",12,("underline bold"))).place(x=10,y=10)
    debit_entry=Entry(screen16,textvariable=debit)
    debit_entry.place(x=410,y=10)
   
    Label(screen16,bg="white",text="ENTER YOUR CARD  EXPIRY DATE(YYYY-MM-DD) ",font=("calibri",12,("underline bold"))).place(x=10,y=70)
    card_entry=Entry(screen16,textvariable=card)
    card_entry.place(x=410,y=70)
    
                    
    Label(screen16,bg="white",text="ENTER YOUR CVV NUMBER",font=("calibri",12,("underline bold"))).place(x=10,y=130)
    card1_entry=Entry(screen16,textvariable=cvv)
    card1_entry.place(x=410,y=130)
    
    Button(screen16,bg="white",text="Pay",font=("calibri",12,("underline bold")),command=final).place(x=300,y=170)
    
    

def final():    
    
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor3=mycon.cursor()
    query3="insert into hotel values('{}','{}','{}','{}','{}','{}','{}')".format(name_1,room_2,room_1,check3_u,checkyo,rooms_1,price3)
    cursor3.execute(query3)
    mycon.commit()
    tkinter.messagebox.showinfo("payment", "You  Booking has  been sucessfull")

def payment3():
    global screen15
    screen15=Toplevel()
    screen15.geometry("740x700")
    screen15.title("payement page")
    screen15.iconbitmap(r'bill_n4I_icon.ico')
    screen15.configure(background="white")
    global room_1
    global room_2
    global name_1
    global check3_u
    global checkyo
    global rooms_1
    
    global price2
    name_1=name4.get()
    room_1=room1.get()
    room_2=room2.get()
    check3_u=checkin5.get()
    checkyo=checkout60.get()
    rooms_1=rooms.get()
    Label(screen15,bg="white",text="BILL",font=("calibri",20,("underline bold")),fg="magenta").grid(row=1,column=2)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="NAME",font=("calibri",14,("underline bold"))).grid(row=4,column=1)
    
    Label(screen15,bg="white",text=name_1,font=("calibri",14,("underline bold"))).grid(row=4,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="ROOM CLASS",font=("calibri",14,("underline bold"))).grid(row=15,column=1)
    Label(screen15,bg="white",text=room_1,font=("calibri",14,("underline bold"))).grid(row=15,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
   
    
    Label(screen15,bg="white",text="ROOM TYPE",font=("calibri",14,("underline bold"))).grid(row=24,column=1)
    Label(screen15,bg="white",text=room_2,font=("calibri",14,("underline bold"))).grid(row=24,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK IN DATE",font=("calibri",14,("underline bold"))).grid(row=33,column=1)
    Label(screen15,bg="white",text=check3_u,font=("calibri",14,("underline bold"))).grid(row=33,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK OUT DATE",font=("calibri",14,("underline bold"))).grid(row=42,column=1)
    Label(screen15,bg="white",text=checkyo,font=("calibri",14,("underline bold"))).grid(row=42,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="NO OF ROOMS BOOKED",font=("calibri",14,("underline bold"))).grid(row=51,column=1)
    Label(screen15,bg="white",text=rooms_1,font=("calibri",14,("underline bold"))).grid(row=51,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
  
    Label(screen15,bg="white",text="PRICE",font=("calibri",14,("underline bold"))).grid(row=60,column=1)
    price2=IntVar()
    
    if room_1== "LUXURY" and room_2=="AC":
        price2=rooms_1*10000
    elif room_1=='EXECUTIVE' and room_2=='AC':
        price2=rooms_1*5000
    elif room_1=='EXECUTIVE' and room_2=='NON AC':
        price2=rooms_1*3000
    Label(screen15,bg="white",text=price2,font=("calibri",14,("underline bold"))).grid(row=60,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="Payment through Corporation-Rupay ",font=("calibri",18,("underline bold"))).grid(row=79,column=2)
    Label(screen15,bg="white",text="*Note please take screenshot of the bill for future reference  ",fg="red").grid(row=80,column=2)
    Label(screen15,bg="white",text="").grid()
    Button(screen15,text="Pay",font=("calibri",12,("underline bold")),relief=GROOVE,command=add_new_user2).grid(row=90,column=2)
    



def add_new_user2():
    global screen16
    screen16=Toplevel()
    screen16.geometry("550x245")
    cv7=tk.Canvas(screen16)
    screen16.title("payment")
    screen16.iconbitmap(r'icon2_emk_icon.ico')
    cv7.pack(side='right', fill='both', expand='yes')
    photo7=PhotoImage(file="epay.png")
    label7=Label(cv7,image=photo7)
    label7.image=photo7
    label7.pack()

   
    global card_entry
    global card1_entry
    global debit_entry
    global debit
    global card
    global cvv
    debit=IntVar()
    cvv=IntVar()
    card=IntVar()
    Label(screen16,bg="white",text="ENTER YOUR DEBIT CARD NUMBER ",font=("calibri",12,("underline bold"))).place(x=10,y=10)
    debit_entry=Entry(screen16,textvariable=debit)
    debit_entry.place(x=410,y=10)
   
    Label(screen16,bg="white",text="ENTER YOUR CARD  EXPIRY DATE(YYYY-MM-DD) ",font=("calibri",12,("underline bold"))).place(x=10,y=70)
    card_entry=Entry(screen16,textvariable=card)
    card_entry.place(x=410,y=70)
    
                    
    Label(screen16,bg="white",text="ENTER YOUR CVV NUMBER",font=("calibri",12,("underline bold"))).place(x=10,y=130)
    card1_entry=Entry(screen16,textvariable=cvv)
    card1_entry.place(x=410,y=130)
    
    Button(screen16,bg="white",text="Pay",font=("calibri",12,("underline bold")),command=final2).place(x=300,y=170)
    
    

def final2():
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor3=mycon.cursor()
    query3="insert into hotel values('{}','{}','{}','{}','{}','{}','{}')".format(name_1,room_2,room_1,check3_u,checkyo,rooms_1,price2)
    cursor3.execute(query3)
    mycon.commit()
    tkinter.messagebox.showinfo("payment", "You  Booking has  been sucessfull")
def payment2():
    global screen15
    screen15=Toplevel()
    screen15.geometry("740x700")
    screen15.title("payement page")
    screen15.iconbitmap(r'bill_n4I_icon.ico')
    screen15.configure(background="white")
    global room_1
    global room_2
    global name_1
    global check3_u
    global checkyo
    global rooms_1
    
    global price1
    name_1=name4.get()
    room_1=room1.get()
    room_2=room2.get()
    check3_u=checkin5.get()
    checkyo=checkout60.get()
    rooms_1=rooms.get()
    Label(screen15,bg="white",text="BILL",font=("calibri",20,("underline bold")),fg="magenta").grid(row=1,column=2)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="NAME",font=("calibri",14,("underline bold"))).grid(row=4,column=1)
    
    Label(screen15,bg="white",text=name_1,font=("calibri",14,("underline bold"))).grid(row=4,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="ROOM CLASS",font=("calibri",14,("underline bold"))).grid(row=15,column=1)
    Label(screen15,bg="white",text=room_1,font=("calibri",14,("underline bold"))).grid(row=15,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
   
    
    Label(screen15,bg="white",text="ROOM TYPE",font=("calibri",14,("underline bold"))).grid(row=24,column=1)
    Label(screen15,bg="white",text=room_2,font=("calibri",14,("underline bold"))).grid(row=24,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK IN DATE",font=("calibri",14,("underline bold"))).grid(row=33,column=1)
    Label(screen15,bg="white",text=check3_u,font=("calibri",14,("underline bold"))).grid(row=33,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK OUT DATE",font=("calibri",14,("underline bold"))).grid(row=42,column=1)
    Label(screen15,bg="white",text=checkyo,font=("calibri",14,("underline bold"))).grid(row=42,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="NO OF ROOMS BOOKED",font=("calibri",14,("underline bold"))).grid(row=51,column=1)
    Label(screen15,bg="white",text=rooms_1,font=("calibri",14,("underline bold"))).grid(row=51,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
  
    Label(screen15,bg="white",text="PRICE",font=("calibri",14,("underline bold"))).grid(row=60,column=1)
    price1=IntVar()
    
    if room_1== "LUXURY" and room_2=="AC":
        price1=rooms_1*10000
    elif room_1=='EXECUTIVE' and room_2=='AC':
        price1=rooms_1*5000
    elif room_1=='EXECUTIVE' and room_2=='NON AC':
        price1=rooms_1*3000
    Label(screen15,bg="white",text=price1,font=("calibri",14,("underline bold"))).grid(row=60,column=3)
    Label(screen15,bg="white",text="").grid()
        

    Label(screen15,bg="white",text="Payment through BOI-Mastercard ",font=("calibri",18,("underline bold"))).grid(row=79,column=2)
    Label(screen15,bg="white",text="*Note please take screenshot of the bill for future reference  ",fg="red").grid(row=80,column=2)
    Label(screen15,bg="white",text="").grid()
    Button(screen15,text="Pay",font=("calibri",12,("underline bold")),relief=GROOVE,command=add_new_user1).grid(row=90,column=2)
    



def add_new_user1():
    global screen16
    screen16=Toplevel()
    screen16.geometry("550x245")
    screen16.iconbitmap(r'icon2_emk_icon.ico')
    cv7=tk.Canvas(screen16)
    cv7.pack(side='right', fill='both', expand='yes')
    photo7=PhotoImage(file="epay.png")
    screen16.title("payment")
    label7=Label(cv7,image=photo7)
    label7.image=photo7
    label7.pack()

   
    global card_entry
    global card1_entry
    global debit_entry
    global debit
    global card
    global cvv
    debit=IntVar()
    cvv=IntVar()
    card=IntVar()
    Label(screen16,bg="white",text="ENTER YOUR DEBIT CARD NUMBER ",font=("calibri",12,("underline bold"))).place(x=10,y=10)
    debit_entry=Entry(screen16,textvariable=debit)
    debit_entry.place(x=410,y=10)
   
    Label(screen16,bg="white",text="ENTER YOUR CARD  EXPIRY DATE(YYYY-MM-DD) ",font=("calibri",12,("underline bold"))).place(x=10,y=70)
    card_entry=Entry(screen16,textvariable=card)
    card_entry.place(x=410,y=70)
    
                    
    Label(screen16,bg="white",text="ENTER YOUR CVV NUMBER",font=("calibri",12,("underline bold"))).place(x=10,y=130)
    card1_entry=Entry(screen16,textvariable=cvv)
    card1_entry.place(x=410,y=130)
    
    Button(screen16,bg="white",text="Pay",font=("calibri",12,("underline bold")),command=final3).place(x=300,y=170)
    
    

def final3():    
    
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor3=mycon.cursor()
    query3="insert into hotel values('{}','{}','{}','{}','{}','{}','{}')".format(name_1,room_2,room_1,check3_u,checkyo,rooms_1,price1)
    cursor3.execute(query3)
    mycon.commit()
    tkinter.messagebox.showinfo("payment", "You  Booking has  been sucessfull")
def payment1():
    global screen15
    screen15=Toplevel()
    screen15.geometry("740x700")
    screen15.title("payement page")
    screen15.iconbitmap(r'bill_n4I_icon.ico')
    screen15.configure(background="white")
    global room_1
    global room_2
    global name_1
    global check3_u
    global checkyo
    global rooms_1
    
    global price
    name_1=name4.get()
    room_1=room1.get()
    room_2=room2.get()
    check3_u=checkin5.get()
    checkyo=checkout60.get()
    rooms_1=rooms.get()
    Label(screen15,bg="white",text="BILL",font=("calibri",20,("underline bold")),fg="magenta").grid(row=1,column=2)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="NAME",font=("calibri",14,("underline bold"))).grid(row=4,column=1)
    
    Label(screen15,bg="white",text=name_1,font=("calibri",14,("underline bold"))).grid(row=4,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="ROOM CLASS",font=("calibri",14,("underline bold"))).grid(row=15,column=1)
    Label(screen15,bg="white",text=room_1,font=("calibri",14,("underline bold"))).grid(row=15,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
   
    
    Label(screen15,bg="white",text="ROOM TYPE",font=("calibri",14,("underline bold"))).grid(row=24,column=1)
    Label(screen15,bg="white",text=room_2,font=("calibri",14,("underline bold"))).grid(row=24,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK IN DATE",font=("calibri",14,("underline bold"))).grid(row=33,column=1)
    Label(screen15,bg="white",text=check3_u,font=("calibri",14,("underline bold"))).grid(row=33,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    
    Label(screen15,bg="white",text="CHECK OUT DATE",font=("calibri",14,("underline bold"))).grid(row=42,column=1)
    Label(screen15,bg="white",text=checkyo,font=("calibri",14,("underline bold"))).grid(row=42,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
    
    Label(screen15,bg="white",text="NO OF ROOMS BOOKED",font=("calibri",14,("underline bold"))).grid(row=51,column=1)
    Label(screen15,bg="white",text=rooms_1,font=("calibri",14,("underline bold"))).grid(row=51,column=3)
    Label(screen15,bg="white",text="").grid()
    Label(screen15,bg="white",text="").grid()
  
    Label(screen15,bg="white",text="PRICE",font=("calibri",14,("underline bold"))).grid(row=60,column=1)
    price=IntVar()
    
    if room_1== "LUXURY" and room_2=="AC":
        price=rooms_1*10000
    elif room_1=='EXECUTIVE' and room_2=='AC':
        price=rooms_1*5000
    elif room_1=='EXECUTIVE' and room_2=='NON AC':
        price=rooms_1*3000
    Label(screen15,bg="white",text=price,font=("calibri",14,("underline bold"))).grid(row=60,column=3)
    Label(screen15,bg="white",text="").grid()
        

    Label(screen15,bg="white",text="Payment through SBI-Mastercard ",font=("calibri",18,("underline bold"))).grid(row=79,column=2)
    Label(screen15,bg="white",text="*Note please take screenshot of the bill for future reference  ",fg="red").grid(row=80,column=2)
    Label(screen15,bg="white",text="").grid()
    Button(screen15,text="Pay",font=("calibri",12,("underline bold")),relief=GROOVE,command=add_new_user).grid(row=90,column=2)
    



def add_new_user():
    global screen16
    screen16=Toplevel()
    screen16.geometry("550x245")
    screen16.iconbitmap(r'icon2_emk_icon.ico')
    screen16.title("payment")
    cv7=tk.Canvas(screen16)
    cv7.pack(side='right', fill='both', expand='yes')
    photo7=PhotoImage(file="epay.png")
    label7=Label(cv7,image=photo7)
    label7.image=photo7
    label7.pack()

   
    global card_entry
    global card1_entry
    global debit_entry
    global debit
    global card
    global cvv
    debit=IntVar()
    cvv=IntVar()
    card=IntVar()
    Label(screen16,bg="white",text="ENTER YOUR DEBIT CARD NUMBER ",font=("calibri",12,("underline bold"))).place(x=10,y=10)
    debit_entry=Entry(screen16,textvariable=debit)
    debit_entry.place(x=410,y=10)
   
    Label(screen16,bg="white",text="ENTER YOUR CARD  EXPIRY DATE(YYYY-MM-DD) ",font=("calibri",12,("underline bold"))).place(x=10,y=70)
    card_entry=Entry(screen16,textvariable=card)
    card_entry.place(x=410,y=70)
    
                    
    Label(screen16,bg="white",text="ENTER YOUR CVV NUMBER",font=("calibri",12,("underline bold"))).place(x=10,y=130)
    card1_entry=Entry(screen16,textvariable=cvv)
    card1_entry.place(x=410,y=130)
    
    Button(screen16,bg="white",text="Pay",font=("calibri",12,("underline bold")),command=final4).place(x=300,y=170)
    
    

def final4():    
    
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor3=mycon.cursor()
    query3="insert into hotel values('{}','{}','{}','{}','{}','{}','{}')".format(name_1,room_2,room_1,check3_u,checkyo,rooms_1,price)
    cursor3.execute(query3)
    mycon.commit()
    tkinter.messagebox.showinfo("payment", "You  Booking has  been sucessfull")
def search():
    global screen9
    global name3
    global name_entry1
    screen9=Toplevel(screen)
    screen9.geometry("400x130")
    screen9.title("search")
    screen9.iconbitmap(r'search_Gvg_icon.ico')
    name3=StringVar()
    Label(screen9,text="ENTER YOUR  FULL NAME(IN CAPS)",font=("calibri",15,("bold underline"))).pack()
    name_entry1=Entry(screen9,textvariable=name3,font=("calibri",15,("bold")))
    name_entry1.pack()
    Label(screen9,text="").pack()
    Button(screen9,text="Next",relief=GROOVE,command=search_next).pack()

def search_next():
    screen9.destroy()
    global screen10
    global checkin3
    global check_in_entry1
    screen10=Toplevel(screen)
    screen10.geometry("400x130")
    screen10.title("search")
    screen10.iconbitmap(r'search_Gvg_icon.ico')
    checkin3=StringVar()
    Label(screen10,text=" ENTER YOUR CHECK IN DATE (YYYY-MM-DD) ",font=("calibri",15,("bold underline"))).pack()
    check_in_entry1=Entry(screen10,textvariable=checkin3,font=("calibri",15,("bold ")))
    check_in_entry1.pack()
    Label(screen10,text="").pack()
    Button(screen10,text="Next",relief=GROOVE,command=search_next2).pack()

def search_next2():
    screen10.destroy()
    global screen11
    global checkout3
    global check_out_entry1
    screen11=Toplevel(screen)
    screen11.geometry("400x130")
    screen11.title("search")
    screen11.iconbitmap(r'search_Gvg_icon.ico')
    checkout3=StringVar()
    Label(screen11,text=" ENTER YOUR CHECK OUT DATE (YYYY-MM-DD)",font=("calibri",15,("bold underline"))).pack()
    check_out_entry1=Entry(screen11,textvariable=checkout3,font=("calibri",15,("bold")))
    check_out_entry1.pack()
    Label(screen11,text="").pack()
    Button(screen11,text="Submit",relief=GROOVE,command=search_find).pack()
    
def search_find():
    screen11.destroy()
    screen12=Tk()
    screen12.geometry("430x330")
    screen12.title("search")
    screen12.configure(background="white")
    screen12.iconbitmap(r'search_Gvg_icon.ico')
    name_=name3.get()
    check1_u=checkin3.get()
    check2_u=checkout3.get()
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor2=mycon.cursor()
    query2=" select * from hotel where name='{}' and check_in='{}' and check_out='{}'".format(name_,check1_u,check2_u)
    cursor2.execute(query2)
    j=cursor2.fetchone()
    if j is not None:
        Label(screen12,text="NAME",font=("calibri",15,("bold")),bg="white").place(x=20,y=0)
        Label(screen12,text=j[0],font=("calibri",15,("bold")),bg="white").place(x=260)
        Label(screen12,text="ROOM TYPE",font=("calibri",15,("bold")),bg="white").place(x=20,y=40)
        Label(screen12,text=j[1],font=("calibri",15,("bold")),bg="white").place(x=260,y=40)
        Label(screen12,text="ROOM CLASS",font=("calibri",15,("bold")),bg="white").place(x=20,y=80)
        Label(screen12,text=j[2],font=("calibri",15,("bold")),bg="white").place(x=260,y=80)
        Label(screen12,text="CHECK IN DATE",font=("calibri",15,("bold")),bg="white").place(x=20,y=120)
        Label(screen12,text=j[3],font=("calibri",15,("bold")),bg="white").place(x=260,y=120)
        Label(screen12,text="CHECK OUT DATE",font=("calibri",15,("bold")),bg="white").place(x=20,y=160)
        Label(screen12,text=j[4],font=("calibri",15,("bold")),bg="white").place(x=260,y=160)
        Label(screen12,text="NO OF ROOMS",font=("calibri",15,("bold")),bg="white").place(x=20,y=200)
        Label(screen12,text=j[5],font=("calibri",15,("bold")),bg="white").place(x=260,y=200)
        Label(screen12,text="PRICE",font=("calibri",15,("bold")),bg="white").place(x=20,y=240)
        Label(screen12,text=j[6],font=("calibri",15,("bold")),bg="white").place(x=260,y=240)
    else:
        screen12.destroy()
        tkinter.messagebox.showerror("search", "No such records are there.Please try again")
        
def cancel():
    global screen8
    screen8=Toplevel(screen)
    screen8.geometry("700x500")
    screen8.title("cancellation page")
    screen8.iconbitmap(r'cancel_oF9_icon.ico')
    photo4=PhotoImage(file="leela-palace-udaipur.png")
    cv4=tk.Canvas(screen8)
    cv4.pack(side='right', fill='both', expand='yes')
    label3=Label(cv4,image=photo4)
    label3.image=photo4
    label3.pack()
    
    global name
    global check_in
    global check_out
    global name_entry
    global check_in_entry
    global check_out_entry
    name=StringVar()
    check_in=StringVar()
    check_out=StringVar()
    Label(screen8,text="Please Enter The Details Below", bg="white",font=("calibri",20,("bold "))).place(x=220,y=10) 

    Label(screen8,text=" ENTER YOUR  FULL NAME (IN CAPS)", bg="white",font=("calibri",16,("bold "))).place(x=10,y=100)
    name_entry=Entry(screen8,textvariable=name,font=("calibri",16,("bold ")))
    name_entry.place(x=450,y=100)
    
    Label(screen8,text=" ENTER YOUR CHECK IN DATE (YYYY-MM-DD)", bg="white",font=("calibri",16,("bold "))).place(x=10,y=200)
    check_in_entry=Entry(screen8,textvariable=check_in,font=("calibri",16,("bold ")))
    check_in_entry.place(x=450,y=200)
   
    
    Label(screen8,text="ENTER YOUR CHECK OUT DATE (YYYY-MM-DD)", bg="white",font=("calibri",16,("bold "))).place(x=10,y=300)
    check_out_entry=Entry(screen8,textvariable=check_out,font=("calibri",16,("bold ")))
    check_out_entry.place(x=450,y=300)
    

    Button(screen8,text="Submit",bg="magenta",font=("calibri",13,("bold")),relief=GROOVE,command=cancel_user).place(x=380,y=390)






def cancel_user():
    global name1
    global check1
    global check2
    
    name1=name.get()
    check1=check_in_entry.get()
    check2=check_out_entry.get()
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor1=mycon.cursor()
    query2="select * from hotel where name='{}' and check_in='{}'and check_out='{}'".format(name1,check1,check2)
    
    cursor1.execute(query2)
    dat1=cursor1.fetchone()
    if dat1 is not None:
        fg()
        
    else:
        tkinter.messagebox.showinfo("cancel","Invalid Information")


def fg():
    mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
    cursor7=mycon.cursor()
    query1="delete  from hotel where name='{}'and check_in='{}'and check_out='{}'".format(name1,check1,check2)
    cursor7.execute(query1)
    mycon.commit()
    Label(screen8,text="Your booking has been successfully cancelled",fg="green",font=("calibri",13,("bold "))).place(x=280,y=450)    

    
 
def view_room():
    class Example(tk.Frame):
        def __init__(self, root):

            tk.Frame.__init__(self, root)
            self.canvas = tk.Canvas(root, borderwidth=30,background="white")
            self.frame = tk.Frame(self.canvas,background="white")
            self.vsb = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.vsb.set)

            self.vsb.pack(side="right", fill="y")
            self.canvas.pack(side="left", fill="both" , expand=True)
            self.canvas.create_window((0,0), window=self.frame, anchor="nw", tags="self.frame")

            self.frame.bind("<Configure>", self.onFrameConfigure)

            self.populate()

        def populate(self):
            mycon=sq.connect(host="localhost",user="root",password="tiger",database="hotel",charset="utf8")
            cursor=mycon.cursor()
            query="select * from hotel "
            cursor.execute(query)
            data=cursor.fetchall()
            Label(self.canvas,text=" Name             room            room_ty           checkin         checkout       no of room        price",font=("calibri" ,15),bg="white").pack()
            j=0
            
            for i in data:
                a,b,c,d,e,f,h=i
                val=Label(self.frame,text=a,bg="white").grid(row=j)
                val1=Label(self.frame,text=b,bg="white").grid(row=j,column=1,ipadx=30)
                val2=Label(self.frame,text=c,bg="white").grid(row=j,column=2,ipadx=36)
                val3=Label(self.frame,text=d,bg="white").grid(row=j,column=3,ipadx=55)
                val4=Label(self.frame,text=e,bg="white").grid(row=j,column=6,ipadx=60)
                val5=Label(self.frame,text=f,bg="white").grid(row=j,column=8,ipadx=44)                
                val6=Label(self.frame,text=h,bg="white").grid(row=j,column=9,ipadx=10)
                j=j+1
      
            
        def onFrameConfigure(self, event):
            '''Reset the scroll region to encompass the inner frame'''
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    if __name__ == "__main__":
        root=tk.Tk()
        root.geometry("849x320")
        root.iconbitmap(r'view_glu_icon.ico')
        root.title("Details")
        Example(root).pack(side="top", fill="both", expand=True)
        root.mainloop()
def main_menu():
    screen6=Toplevel()
    screen6.title("Main menu")
    screen6.geometry("5000x5000")
    screen6.iconbitmap(r'icon_gtp_icon.ico')
    photo3=PhotoImage(file="Luxury-Hotels-in-India (1).png")
    cv3 = tk.Canvas(screen6)
    cv3.pack(side='right', fill='both', expand='yes')
    label2=Label(cv3,image=photo3)
    label2.image=photo3
    label2.pack()
    Label(screen6,text="WELCOME TO THE CLASSICO HOTEL", fg="green",font=("Italics",30,("underline bold"))).place(x=290,y=0)
    Button(screen6,text="BOOK A ROOM",height="5",width="20",bg="red",font=("calibri",13,("bold ")),relief=GROOVE,command=booking).place(x=390,y=100)
    Button(screen6,text="CANCEL YOUR BOOKING",height="5",width="20",bg="blue",font=("calibri",13,("bold ")),relief=GROOVE,command=cancel).place(x=790,y=100)
    Button(screen6,text="VIEW DETAILS",height="5",width="20",bg="yellow",font=("calibri",13,("bold ")),relief=GROOVE,command=view_room).place(x=390,y=400)
    Button(screen6,text="VIEW YOUR BOOKING",height="5",width="20",bg="magenta",font=("calibri",13,("bold ")),relief=GROOVE,command=search).place(x=790,y=400)
    
def login():
    global screen2
    screen2=Toplevel(screen)
    screen2.geometry("390x250")
    screen2.title("login")
    screen2.iconbitmap(r'login_Tc6_icon.ico')
    photo2=PhotoImage(file="sun.png")
    cv2=tk.Canvas(screen2)
    cv2.pack(side='right', fill='both', expand='yes')
    label1=Label(cv2,image=photo2)
    label1.image=photo2
    label1.pack()



    
    Label(screen2,text="Please enter details below to login", bg="white",font=("Calibri",13)).place(x=90,y=0)
    global username_entry1
    global password_entry1
    global username_verify
    global password_verify
    username_verify=StringVar()
    password_verify=StringVar()
    Label(screen2,text="Username", bg="white",font=("calibri",11)).place(x=50,y=60)
    username_entry1=Entry(screen2,textvariable=username_verify,font=("calibri",11))
    username_entry1.place(x=190,y=60)

    
    Label(screen2,text="Password", bg="white",font=("calibri",11)).place(x=50,y=118)
    password_entry1=Entry(screen2,textvariable=password_verify,font=("calibri",11))
    password_entry1.place(x=190,y=118)
    
    
    Button(screen2,text="Login",bg="magenta",width=10,height=1,relief=GROOVE,font=("calibri",11),command=login_verify).place(x=120,y=160)
def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_file=os.listdir()
    if username1 in list_of_file:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            main_menu()
        else:
            a=Label(screen2,text="Password not found",bg="red",font=("calibri",10)).place(x=103,y=200)
            
           
    else:
        Label(screen2,text="user not found",bg="red",font=("calibri",10)).place(x=113,y=225)      
def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("390x240")
    screen1.iconbitmap(r'login_Tc6_icon.ico')
    photo1=PhotoImage(file="abstract.png")
    cv1=tk.Canvas(screen1)
    cv1.pack(side='right', fill='both', expand='yes')
    label=Label(cv1,image=photo1)
    label.image=photo1
    label.pack()
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    Label(screen1,text="Please enter details below", bg="white",font=("calibri",13)).place(x=90,y=0)
    
    Label(screen1,text="Username", bg="white",font=("calibri",11)).place(x=50,y=60)

    username_entry=Entry(screen1,textvariable=username,font=("calibri",11))
    username_entry.place(x=190,y=60)

    b=Label(screen1,text="Password", bg="white",font=("calibri",11)).place(x=50,y=118)
    password_entry=Entry(screen1,textvariable=password,font=("calibri",11))
    password_entry.place(x=190,y=118)

    Button(screen1,text="Register",bg="pink",width=10,height=1,font=("calibri",11),relief=GROOVE,command=register_user).place(x=120,y=180)
    
def register_user():
    username_info=username.get()
    password_info=password.get()
    file=open(username_info,"w")
    file.write(password_info+"\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0,END)
    password_entry.delete(0,END)
    Label(screen1,text="Registeration success", bg="white",fg="green",font=("calibri",10)).place(x=100,y=215)

def mainscreen():
    global screen
    screen=Tk()
    screen.title('login')
    #photo=PhotoImage(file="dd.png")
    screen.geometry("300x300")
    screen.iconbitmap(r'hooome_xcJ_icon.ico')
    cv = tk.Canvas(screen)
    cv.pack(side='right', fill='both', expand='yes')
    #Label(cv,image=photo).pack()
    Label(screen,text="Welcome", fg="green",bg="magenta",width=35,height=2,font=("calibri",13)).place(x=0,y=0)
    Button(screen,text="Login",bg="silver",height="2",width="30", relief=GROOVE,command=login).place(x=29,y=76)
    Button(screen,text="Register",bg="gold",height="2",width="30",relief=GROOVE,command=register).place(x=29,y=165)
    screen.mainloop()
mainscreen()   
    
