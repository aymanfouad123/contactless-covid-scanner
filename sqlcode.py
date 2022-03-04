from tkinter import *
from tkinter import ttk     #styles
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import sys
import os
import mysql.connector
from mysql.connector import errorcode


connection = mysql.connector.connect(user='freedbtech_dscproject', password='dscdevice',host='freedb.tech',port=3306,database='freedbtech_Associatesdata')

#import Temperature_Sensor
#import scanner_code

average_temp=0
def restart_program():   #After Exit button
        python = sys.executable
        os.execl(python, python, * sys.argv)

def callback(url):       #open url fucntion
        webbrowser.open_new(url)
#Window 1
def main():
    connection.commit()
    Selected_Ans1=0
    Selected_Ans2=0
    Selected_Ans3=0
    win=Tk()
    s=ttk.Style()
    win.state("zoomed")

    canvas = Canvas(win, width=800, height=450)
    canvas.grid(columnspan=3, rowspan=3)

    win.title("Contacltless Self Scanning Device")

    #logo
    logo = Image.open('logo.png')
    logo = logo.resize((130, 50))
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo)
    logo_label.image = logo
    logo_label.place(x=0,y=0)
  
    #Question 1
    Q1=Label(win,text="Have you had any Covid-19 related symptoms :(dry cough, fever, tiredness)?")
    Q1.place(x=10,y=80)
    Ans1=IntVar()
    Ans1.set(2)
    Q1_Op1=Radiobutton(win,text="Yes", variable=Ans1,value=1)
    Q1_Op1.place(x=600,y=100)
    Q1_Op2=Radiobutton(win,text="No", variable=Ans1,value=2)
    Q1_Op2.place(x=650,y=100)

    #Question 2
    Q2=Label(win,text="Have you been outside of Canada in the past 14 days?")
    Q2.place(x=10,y=150)
    Ans2=IntVar()
    Ans2.set(2)
    Q2_Op1=Radiobutton(win,text="Yes", variable=Ans2,value=1)
    Q2_Op1.place(x=600,y=170)
    Q2_Op2=Radiobutton(win,text="No", variable=Ans2,value=2)
    Q2_Op2.place(x=650,y=170)

    #Question 3
    Q3=Label(win,text="Have you had any contact with a confirmed Covid-19 case, or caring for someone diagnosed with Covid-19?")
    Q3.place(x=10,y=220)
    Ans3=IntVar()
    Ans3.set(2)
    Q3_Op1=Radiobutton(win,text="Yes", variable=Ans3,value=1)
    Q3_Op1.place(x=600,y=250)
    Q3_Op2=Radiobutton(win,text="No", variable=Ans3,value=2)
    Q3_Op2.place(x=650,y=250)


    def evaluate():
        global Selected_Ans1,Selected_Ans2,Selected_Ans3
        Selected_Ans1=int(Ans1.get())
        Selected_Ans2=int(Ans2.get())
        Selected_Ans3=int(Ans3.get())
        win.destroy()

    button1=Button(win,text="Next", command=evaluate, font="Raleway", highlightbackground="#20bebe", fg="white", height=2, width=15).place(x=50,y=330)

    
    sql_select_Query1 = "select * from info"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query1)
    records = cursor.fetchall()
    check_in_list=[]
    for row in records:
         check_in=row[8].strip('}')
         check_in_list.append(check_in)
    if "Warning" in check_in_list:
        win.configure(bg='red')
        Label(win,text="Someone in the store is in danger and could be a risk for others, please Call a manager to log in and check !").place(x=100,y=400)
        messagebox.showinfo("Danger","Someone in the store is in danger and could be a risk for others, please Call a manager to log in and check !")
    def see_data():
        #show who did and did not do their temp checks
        admin_barcode=[123454324]
        #scanner=scanner_code.scanner()
        scanner=123454324  #test
        messagebox.showinfo("Attention","Please scan your Badge barcode")
        if scanner in admin_barcode:
            connection.commit()
            sql_select_Query1 = "select * from info"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query1)
            records = cursor.fetchall()
            check_done=[]
            check_not_done=[]
            temp_list=[]
            for row in records:
                id_num=row[0]
                Firstname=row[1].strip('}')
                Lastname=row[2].strip('}')
                position=row[3].strip('}')
                barcode=row[4]
                start_time=row[5].strip('}')
                end_time=row[6].strip('}')
                temp=row[7]
                check_in=row[8].strip('}')

                temp_list.append(id_num)
                temp_list.append(Firstname)
                temp_list.append(Lastname)
                temp_list.append(position)
                temp_list.append(start_time)
                temp_list.append(end_time)
                

                if check_in=="Done" or check_in=="Warning": 
                    temp_list.append(temp)
                    temp_list.append(check_in)
                    check_done.append(temp_list)
                else:
                    temp_list.append("No Temperature recorded")
                    temp_list.append("Not Done")
                    check_not_done.append(temp_list)

                temp_list=[]

            #Display data Window
            admin_window=Toplevel(win)
            admin_window.state("zoomed")
            y1=40
            y2=40
            for i in check_done:
                display=(str(i[1]) + " " + str(i[2]) + " " +str(i[3])+ " " +str(i[4])+ " " +str(i[5])+ " " +str(i[6])+ " " +str(i[7]))
                Label(admin_window,text=display).place(x=0,y=y1)
                y1+=20
            for i in check_not_done:
                display=(str(i[1]) + " " + str(i[2]) + " " +str(i[3])+ " " +str(i[4])+ " " +str(i[5])+ " " +str(i[6])+ " " +str(i[7]))
                Label(admin_window,text=display).place(x=300,y=y2)
                y2+=20

            Button(admin_window,text="Go Back", command=restart_program).place(x=0,y=0)
        else:
            messagebox.showinfo( "Warning", "You are not an athorized personnel")


    Button(win,text="Admin log in", command=see_data, font="Raleway", highlightbackground="#20bebe", fg="white", height=2, width=15).place(x=50,y=380)


    win.mainloop()

main()


        
def warning(average_temp):           #warning window
    connection.commit()
    Label(win2,text="Return Home Immedietly !, It is not safe for you to work, it is important that you self isolate and seek testing. Please review the Covid-19").place(x=20,y=50)
    Label(win2,text="please scan your barcode").place(x=100,y=200)
    #scanner=scanner_code.scanner()
    scanner=2147483647
    update="UPDATE info SET temp=%(average_temp)s, check_in='Warning' WHERE barcode_num=%(scanner)s"
    cursor = connection.cursor()
    cursor.execute(update,{ 'average_temp': average_temp, 'scanner': scanner })
    connection.commit()
    button2=Button(win2,text="Exit", command=restart_program).place(x=50,y=200)

    #link = Label(win2, text="public health measures", fg="blue", cursor="hand2")
    #link.pack()
    #link.bind("<Button-1>", lambda e: callback("http://covid-19.ontario.ca"))




#Window 2
win2=Tk()
win2.state("zoomed")
win2.title("Contacltless Self Scanning Device")
canvas = Canvas(win2, width=600, height=250)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png')
logo = logo.resize((130, 50))
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.place(x=0,y=0)

if Selected_Ans1==2 and Selected_Ans2==2 and Selected_Ans3==2: 
    label=Label(win2,text="Please be within 10cm away from the sensor")
    label.place(x=5,y=60)
    
    def nextp():
        win2.destroy()

    #average=Temperature_Sensor.run_sensor()

    average_temp=36  #test

    if average_temp>=36 and average_temp<38:
        button3=Button(win2,text="Next", command=nextp, font="Raleway", highlightbackground="#20bebe", fg="white", height=2, width=15).place(x=30,y=160)
        #we could update the temps in thr database later
        pass_=True
    else:
        label.destroy()
        messagebox.showinfo( "Warning", "Your temperature is too high, Please go home and let a manager be aware of this !")
        warning(average_temp)

elif Selected_Ans1!=0 and Selected_Ans2!=0 and Selected_Ans3!=0:
    messagebox.showinfo( "Warning", "You are not allowed to start you shift, Please contact your manager !")
    warning(average_temp)

win2.mainloop()


#Window 3 based on %pass_ 
if pass_==True:
    win3=Tk()
    win3.state("zoomed")
    canvas = Canvas(win3, width=600, height=350)
    canvas.grid(columnspan=3, rowspan=3)
    win3.title("Contacltless Self Scanning Device")
    #logo
    logo = Image.open('logo.png')
    logo = logo.resize((130, 50))
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo)
    logo_label.image = logo
    logo_label.place(x=0,y=0)
    #scanner=scanner_code.scanner()
    scanner=2147483647
    Label(win3,text="Please scan your barcode").place(x=1,y=60)

    try:
        connection.commit()
        #Getting values from table of the day 
        sql_select_Query = "select * from info where barcode_num=%(scanner)s"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query,{ 'scanner': scanner })
        records = cursor.fetchall()
        for row in records:
            id_num=row[0]
            Firstname=row[1].strip('}')
            Lastname=row[2].strip('}')
            position=row[3].strip('}')
            barcode=row[4]
            start_time=row[5].strip('}')
            end_time=row[6].strip('}')

        def update_data():      #update the temp and check_in into table
            update="UPDATE info SET temp=%(average_temp)s, check_in='Done' WHERE barcode_num=%(scanner)s"
            cursor = connection.cursor()
            cursor.execute(update,{ 'average_temp': average_temp, 'scanner': scanner })
            connection.commit()
            restart_program()

        lbl2=Label(win3,text="Please confirm your shift")
        lbl2.place(x=20,y=90)
        but=(Firstname + ' '+ Lastname+', '+ position+ ', Shift: '+ start_time+ ' To '+ end_time)
        button4=Button(win3,text=(but), command=update_data).place(x=40,y=130)

    except NameError:
        Label(win3,text="Nothing matches the barcode scanned, no shift for you today").place(x=50,y=90)
        lbl2.destroy()

    Button(win3,text="Exit", command=restart_program, font="Raleway", highlightbackground="#20bebe", fg="white", height=2, width=15).place(x=50,y=250)
    
    win3.mainloop()



connection.close()
