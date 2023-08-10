from tkinter import *
# import mysql
# db=mysql.connector.connect(host="localhost",user="root",password="",db="eb_bill")
# cursor=db.cursor()
class Mainframe:
    def __init__(self,root):
        self.root=root
        self.root.title("EB  login")
        self.root.geometry("850x450")
        self.root.resizable(False,False)
        self.root.configure(bg="white")
        self.userlabel=Label(self.root,text="EB User Login",font=("Impact",25),fg="#00008B",bg="white")
        self.userlabel.place(x=68,y=25)
        self.adminlabel=Label(self.root,text="Admin Login",font=("Impact",20),fg="#151B54",bg="white")
        self.adminlabel.place(x=450+5,y=25)
        separator=Frame(self.root,bg="navy blue")
        separator.place(x=250+10+4,height=430,width=0+2)
        separator2=Frame(self.root,bg="#DC143C")
        separator2.place(y=350+10+4,x=100,width=650,height=0+2)
        separator3=Frame(self.root,bg="hot pink")
        separator3.place(y=180+10+4,width=400,height=0+1)
        separator4=Frame(self.root,bg="#78C7C7")
        separator4.place(x=550+10+4,height=400,width=0+1)
        separator5=Frame(self.root,bg="#C24641")
        separator5.place(x=500,y=200+10+4,width=400,height=0+1)
        userframe=Frame(self.root,bg="#95B9C7",relief=RIDGE)
        userframe.place(x=70,y=70,width=350,height=250)
        adminframe=Frame(self.root,bg="#E75480")
        adminframe.place(x=450,y=70,width=350,height=200)
        quitframe=Frame(self.root,bg="#C9C0BB")
        quitframe.place(width=130,height=30+2+5,x=715,y=350+10+3+4)

        self.admin=Label(adminframe,text="Admin ",font=("Arial Black",10),fg="white",bg="#E75480")
        self.admin.place(x=25,y=30)
        self.admin_entry=Entry(adminframe,width=20)
        self.admin_entry.place(x=138,y=28)
       
        self.adminpwd=Label(adminframe,text="Password",font=("Arial Black",10),fg="white",bg="#E75480")
        self.adminpwd.place(x=25,y=70)
        self.adminpwd_entry=Entry(adminframe,width=25)
        self.adminpwd_entry.place(x=138,y=70)
        
        self.loginbtn=Button(adminframe,text="Login",font=("helvetica",10,"bold"),bg="#F8F8FF",fg="#033E3E",command=self.adminlogin,width=10)
        self.loginbtn.place(x=110,y=140)
        self.quitbtn=Button(quitframe,text="Quit",font=("helvetica",10,"bold"),bg="#F8F8FF",fg="blue",command=self.Quit,width=10)
        self.quitbtn.pack()

        
        self.ebnum=Label(userframe,text="EB num",font=("Arial Black",10),fg="#123456",bg="#95B9C7")
        self.ebnum.place(x=25,y=30)
        self.ebnum_entry=Entry(userframe)
        self.ebnum_entry.place(x=138,y=28)
        self.password=Label(userframe,text="Password",font=("Arial Black",10),fg="#123456",bg="#95B9C7")
        self.password.place(x=25,y=70)
        self.password_entry=Entry(userframe,show="*",width=25)
        self.password_entry.place(x=138,y=70)
        self.loginbtn=Button(userframe,text="Login",font=("helvetica",10,"bold"),bg="#F8F8FF",fg="#00008B",command=self.login,width=10)
        self.loginbtn.place(x=110,y=140)
        self.newuserbtn=Button(userframe,text="New user signup...",font=("optima",11),bd=0,bg="#95B9C7",command=self.register)
        self.newuserbtn.place(x=98,y=100)
    def login(self):
        if self.ebnum_entry.get()=="" or self.password_entry.get()=="":
            print("All fields are required")
        else:
            try:
                cursor.execute("SELECT * FROM users WHERE ebnum=%s AND password=%s", (self.ebnum_entry.get(),self.password_entry.get()))
                row=cursor.fetchone()
                if row== None :
                    print("user not found")
                else:
                    print("user exixted")
                    self.pay()
                    self.root.withdraw()
            except Exception as es :
                print("error due to",es)
    def pay(self):        
        def paylogout():
            pay.destroy()
            self.root.deiconify()
        def paybill():
            sql="INSERT INTO paymentdetails(ebnum,amount) VALUES(%s,%s) "
            val=(ebnum,a)
            cursor.execute(sql,val)
            db.commit()
        pay=Toplevel(self.root)
        pay.geometry("800x600")
        pay.title("paybill")
        pay.resizable(False,False)
        pay.configure(bg="white")
        label=Label(pay,text="Bill Payment Portal",font=("Impact",25),fg="#00008B",bg="white")
        label.place(x=70,y=10)
        frame=Frame(pay,bg="#79BAEC",highlightbackground="#3B9C9C")
        frame.place(x=100,y=70,width=600,height=500)
        bottomframe=Frame(frame,bg="#151B54")
        bottomframe.place(width=600,height=50,y=380+35+3)
        bottomlabel=Label(bottomframe,text="Online EB Payment",font=("Eras Bold ITC",10,"bold"),fg="white",bg="#151B54")
        bottomlabel.place(x=445+2)

        scrolllabel=Label(frame,text="Pay History",font=("Britannic Bold",15,"bold"),fg="#29465B",bg="#79BAEC")
        scrolllabel.place(x=150,y=180+10+4+6)
        scrollframe=Frame(frame,height=100,width=30,bg="red")
        scrollframe.place(x=150,y=230)
        sb=Scrollbar(scrollframe,bg="black")
        sb.pack(side=RIGHT,fill=Y)
        mylist=Listbox(scrollframe,yscrollcommand=sb.set,height=10,width=25)
        ebnum=self.ebnum_entry.get()
        sql="SELECT amount FROM paymentdetails WHERE ebnum=%s"
        val=(ebnum,)
        cursor.execute(sql,val)
        payhistory=cursor.fetchall()
        for line in  payhistory:
            mylist.insert(END," ",line)
        mylist.pack(side=LEFT)
        sb.config(command=mylist.yview)
        
        topseparator=Frame(frame,bg="white")
        topseparator.place(x=300,y=30+10+4,width=400,height=2)
        logoutbttn=Button(frame,text="Logout",font=("kabel ult BT",10,"bold"),width=8,bg="#CCCCFF",command=paylogout)
        logoutbttn.place(x=400,y=200)

        sql=(" SELECT ebuser FROM users WHERE ebnum=%s")
        val=(self.ebnum_entry.get(),)
        cursor.execute(sql,val)
        user=cursor.fetchone()
        userlabel=Label(frame,text=('User  |'),font=("impact",15),bg="#79BAEC")
        userlabel.place(x=350,y=5)
        username=Label(frame,text=user,font=("Arial Black",15),bg="#79BAEC")
        username.place(x=410+5+10+3,y=5)
        sql=(" SELECT ebamount FROM users WHERE ebnum=%s")
        val=( self.ebnum_entry.get(),)
        cursor.execute(sql,val)
        amount=cursor.fetchone()
        Amount2=amount
        for a in Amount2:
            btn=Button(frame,text="Pay",font=("kabel ult BT",10,"bold"),bg="#CCCCFF",width=8,command=paybill)
            btn.place(x=400,y=150)
        bill_label=Label(frame,text="Bill amount for this month",font=("helvetica",15),bg="#79BAEC")
        bill_label.place(x=45,y=130)
        bill=Label(frame,text=amount,font=("helvetica",17,"underline"),bg="#79BAEC")
        bill.place(x=280,y=125)
        sql=(" SELECT units FROM users WHERE ebnum=%s")
        val=(self.ebnum_entry.get(),)
        cursor.execute(sql,val)
        units=cursor.fetchone()
        unitslabel=Label(frame,text="Units Consumed-",font=("helvetica",15),bg="#79BAEC")
        unitslabel.place(x=45,y=80)
        units=Label(frame,text=units,font=("helvetica",15),bg="#79BAEC")
        units.place(x=200,y=80)
        ebnum=self.ebnum_entry.get()
    def adminlogin(self):
        if self.admin_entry.get()=="" or self.adminpwd_entry.get()=="":
            print("All fields are required")
    #_____________________admin user and password___________________
        elif self.admin_entry.get()=="siva" and self.adminpwd_entry.get()=="12345":
   #| ___________________________________________________________|
                    print("Admin")
                    self.adminpanel()
        else:
            print(" access denied")
          #Close application____
    def Quit(self):
        self.root.destroy()
        db.close()
    #_________________
    def adminpanel(self):
        self.adminWindow=Toplevel(self.root)
        self.admin=Admin(self.adminWindow)
        self.adminWindow.grab_set()
    def register(self):
        self.registerWindow=  Toplevel(self.root)
        self.register=Registration(self.registerWindow)
        self.registerWindow.grab_set()
class Admin():
    def __init__(self,root):
        self.root=root
        self.root.title("Admin")
        self.root.geometry("450x250")
        self.root.resizable(False,False)
        scrollframe=Frame(self.root,height=100,width=30,bg="red")
        scrollframe.place(x=250,y=40)
        sb=Scrollbar(scrollframe,bg="black")
        sb.pack(side=RIGHT,fill=Y)
        mylist=Listbox(scrollframe,yscrollcommand=sb.set,height=10,width=25)
        cursor.execute("SELECT ebuser  ,  ebnum FROM users")
        user=cursor.fetchall()
        for line in  user:
            mylist.insert(END," ",line)
        mylist.pack(side=LEFT)
        sb.config(command=mylist.yview)
        listlabel=Label(self.root,text="User       EBnum",font=("bold"))
        listlabel.place(x=280,y=15)
        self.label=Label(self.root,text="User ebnum")
        self.label.place(x=25,y=25)
        self.existebnum=Entry(self.root)
        self.existebnum.place(x=100,y=25)
        self.label2=Label(self.root,text="Amount")
        self.label2.place(x=50,y=75)
        self.update_amount=Entry(self.root)
        self.update_amount.place(x=100,y=75)
        self.label3=Label(self.root,text="Units")
        self.label3.place(x=65,y=120)
        self.unit=Entry(self.root)
        self.unit.place(x=100,y=120)
        self.submitbtn=Button(self.root,text="submit",bg="grey",fg="black",command=self.updatebill,width=8)
        self.submitbtn.place(x=130,y=150)
    def updatebill(self):
        if self.existebnum.get()=="" or self.update_amount.get()=="":
            print("All fields are required")
        else:
            try:
                cursor.execute("SELECT ebnum FROM users WHERE ebnum=%s", (self.existebnum.get(),))
                user=cursor.fetchone()
                if user== None :
                    print("user not found")
                else:
                    #UPDATE `users` SET `ebamount`='2000' WHERE ebnum='99429454280'
                    sql= "UPDATE users SET ebamount = %s ,units=%s WHERE ebnum= %s "
                    val=(self.update_amount.get(),self.unit.get(),self.existebnum.get(),)
                    cursor.execute(sql,val)
                    db.commit()
                    print(cursor.rowcount,"record(s) affected")
            except Exception as es :
                print("error due to",es)
class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("New Register")
        self.root.geometry("600x400")
        self.root.resizable(False,False)
        self.root.configure(bg="white")
        self.mainlabel=Label(self.root,text="Registration",font=("Impact",25),fg="#00008B",bg="white")
        self.mainlabel.place(x=140,y=25)
        
        frame=Frame(self.root,bg="#95B9C7",highlightbackground="#3B9C9C")
        frame.place(x=150,y=70,width=340,height=300)

        self.new_username=Label(frame,text="Username",font=("Arial Black",10,"bold"),fg="#123456",bg="#95B9C7")
        self.new_username_entry=Entry(frame,width=25)
        
        self.new_user_pwd=Label(frame,text="Password",font=("Arial Black",10),fg="#123456",bg="#95B9C7")
        self.new_userpwdche=Label(frame,text=" Confirm Password",font=("Arial Black",10),fg="#123456",bg="#95B9C7")

        self.new_user_ebnum=Label(frame,text="EB number",font=("Arial Black",10),fg="#123456",bg="#95B9C7")
        self.new_user_ebnum_entry=Entry(frame,width=25)
        
        self.new_userpwd_entry=Entry(frame,width=25)
        self.new_userpwdche_entry=Entry(frame,width=25)

        self.newuserbtn=Button(frame,text="Register",font=("helvetica",10,"bold"),fg="#F8F8FF",bg="#CA226B",bd=1,command=self.register,width=10)
        self.newuserbtn.place(x=130,y=200)

        self.loginframe=Button(frame,text="login..",font=("optima",11),bd=0,bg="#95B9C7",width=10,command=self.loginframe)
        self.loginframe.place(x=130,y=230)

        self.new_user_ebnum.place(x=15,y=150)
        self.new_user_ebnum_entry.place(x=160,y=150)
        
        self.new_username.place(x=15,y=30)
        self.new_username_entry.place(x=160,y=28)

        self.new_user_pwd.place(x=15,y=70)
        self.new_userpwd_entry.place(x=160,y=70)

        self.new_userpwdche.place(x=10,y=110)
        self.new_userpwdche_entry.place(x=160,y=110)
    def loginframe(self):
        self.root.destroy()
    def register(self):
        sql="INSERT INTO users(ebuser,password,ebnum)VALUES(%s,%s,%s)"
        val=(self.new_username_entry.get(),self.new_userpwd_entry.get(),(self.new_user_ebnum_entry.get()))
        if self.new_username_entry.get()=="" or self.new_userpwd_entry.get()=="":
            print("All fields are required")
        elif len(self.new_username_entry.get()) <=5 or len(self.new_username_entry.get())>=20:
            print("Enter valid username")
        elif self.new_userpwd_entry.get() != self.new_userpwdche_entry.get():
            print("Password mismatch")
        elif len(self.new_user_ebnum_entry.get()) !=11:
            print("enter your valid ebnumber")
        else:
        #=====================registration mysql query==============================
            try:
                che_sql=("SELECT ebnum FROM users WHERE ebnum=%s" )
                che_data=(self.new_user_ebnum_entry.get(),)
                cursor.execute(che_sql,che_data)
                ebnum=cursor.fetchone()
                if  ebnum == None:
                    cursor.execute(sql,val)
                    db.commit()
                    print("registered")
                    self.root.destroy()
                else:
                    print("give the eb number belongs to you")
            except Exception as es :
                  print("error due to",es)
def main():
    root=Tk()
    Register=Mainframe(root)
    Admin=Mainframe(root)
    root.mainloop()
if __name__=='__main__':
    main()
