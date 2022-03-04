import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

#Background
#backimage = tk.PhotoImage(file = "Background.png")
#backlabel = tk.Label(root , image = backimage)
#backlabel.place(relwidth = 1 , relheight = 1)

def mainpage():

    root = tk.Tk()
    root.title("Contacltless Self Scanning Device")
    canvas = tk.Canvas(root, width=650, height=300)
    canvas.grid(columnspan=3, rowspan=3)
    #logo
    logo = Image.open('logo.png')
    logo = logo.resize((400, 150))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.grid(column=1, row=0)

    #instructions
    instructions = tk.Label(root, text="Fill In Your Credentials", font="Raleway")
    instructions.grid(columnspan=3, column=1, row=1)
    #Username 
    login_user = tk.Label(root ,text = "Your Username -")
    login_user.grid(columnspan = 3 ,column = 1, row = 2)
    login_entry = tk.Entry(root)
    login_entry.grid(columnspan = 3,column=1,row =3)

    space = tk.Label(root,text = "")
    space.grid(columnspan = 3 ,column = 1, row = 4)

    #Password
    pass_user = tk.Label(root,text = "Your Password -")
    pass_user.grid(columnspan = 3 ,column = 1, row = 5)
    pass_entry = tk.Entry(root)
    pass_entry.grid(columnspan = 3,column=1,row =6)

    space2 = tk.Label(root,text = "")
    space2.grid(columnspan = 3 ,column = 1, row = 7)
    space3 = tk.Label(root,text = "")
    space3.grid(columnspan = 3 ,column = 1, row = 8)

    def button_click(username,password):
        print(username)
        print(password)
        root.destroy()
        
    #browse button
    browse_text = tk.StringVar()
    browse_btn = tk.Button(root, textvariable=browse_text, command=lambda : button_click(login_entry.get(),pass_entry.get()), font="Raleway", highlightbackground="#20bebe", fg="white", height=2, width=15)
    browse_text.set("Enter")
    browse_btn.grid(columnspan = 3,column=1, row=9)

    canvas = tk.Canvas(root, width=650, height=100)
    canvas.grid(columnspan=3)

    root.mainloop()





mainpage()

def page2():
    Selected_Ans1=0
    Selected_Ans2=0
    Selected_Ans3=0

    win=tk.Tk()
    canvas = tk.Canvas(win, width=800, height=450)
    canvas.grid(columnspan=3, rowspan=3)
    win.title("Contacltless Self Scanning Device")

    #logo
    logo = Image.open('logo.png')
    logo = logo.resize((130, 50))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.place(x=0,y=0)
    
    #Question 1
    Q1=tk.Label(win,text="Have you had any Covid-19 related symptoms :(dry cough, fever, tierdness)?")
    Q1.place(x=10,y=80)
    Ans1=tk.IntVar()
    Ans1.set(2)
    Q1_Op1=tk.Radiobutton(win,text="Yes", variable=Ans1,value=1)
    Q1_Op1.place(x=600,y=100)
    Q1_Op2=tk.Radiobutton(win,text="No", variable=Ans1,value=2)
    Q1_Op2.place(x=650,y=100)

    #Question 2
    Q2=tk.Label(win,text="Have you been outside of Canada in the past 14 days?")
    Q2.place(x=10,y=150)
    Ans2=tk.IntVar()
    Ans2.set(2)
    Q2_Op1=tk.Radiobutton(win,text="Yes", variable=Ans2,value=1)
    Q2_Op1.place(x=600,y=170)
    Q2_Op2=tk.Radiobutton(win,text="No", variable=Ans2,value=2)
    Q2_Op2.place(x=650,y=170)

    #Question 3
    Q3=tk.Label(win,text="Have you had any contact with a confirmed Covid-19 case, or caring for someone diagnosed with Covid-19?")
    Q3.place(x=10,y=220)
    Ans3=tk.IntVar()
    Ans3.set(2)
    Q3_Op1=tk.Radiobutton(win,text="Yes", variable=Ans3,value=1)
    Q3_Op1.place(x=600,y=250)
    Q3_Op2=tk.Radiobutton(win,text="No", variable=Ans3,value=2)
    Q3_Op2.place(x=650,y=250)

    def evaluate():
        global Selected_Ans1,Selected_Ans2,Selected_Ans3
        Selected_Ans1=int(Ans1.get())
        Selected_Ans2=int(Ans2.get())
        Selected_Ans3=int(Ans3.get())
        win.destroy()

    browse_text = tk.StringVar()
    browse_text.set("Next")
    browse_btn = tk.Button(win, textvariable=browse_text, command=evaluate, font="Raleway", highlightbackground="#20bebe", fg="white", height=2, width=15)
    browse_btn.place(x=300,y=300)
    

    win.mainloop()



    
page2()    

def page3():
    win2=tk.Tk()
    win2.title("Contacltless Self Scanning Device")
    canvas = tk.Canvas(win2, width=800, height=250)
    canvas.grid(columnspan=3, rowspan=3)
    
    #logo
    logo = Image.open('logo.png')
    logo = logo.resize((100, 50))
    logo = ImageTk.PhotoImage(logo)
    logo_label = tk.Label(image=logo)
    logo_label.image = logo
    logo_label.place(x=0,y=0)
    
    label=tk.Label(win2,text="Please be within 10cm away from the sensor")
    label.place(x=1,y=70)
    
def checkcorrect():
    global Selected_Ans1,Selected_Ans2,Selected_Ans3
    
    if Selected_Ans1==2 or Selected_Ans2==2 or Selected_Ans3==2: 
        page3()
    else:
        page2()
        
checkcorrect()











    
