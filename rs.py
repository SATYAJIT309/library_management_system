from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter 




class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

         #========================================variable====================================================
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastnane_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar() 
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar() 
        self.dateoverdue_var=StringVar()
        self.finallprice_var=StringVar()

        lbltitle = Label (self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,'bold'),padx=2,pady=6)
        lbltitle.pack(side = TOP,fill=X)


        frame = Frame(self.root,bd=12,relief = RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1440,heigh=400)


       #--------------------------dataframeleft------------------------------------

        DataFrameLeft=LabelFrame(frame,text="libraryMemberInformation",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("time new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=850,height=360)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="member type:",font=("arial",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("arial",12,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staf","Student","Lecturer")
        comMember.grid(row=0,column=1)

        lblPRN_No=Label(DataFrameLeft,font=("arial",12,"bold"),text="PRN NO:",padx=2,pady=6,bg="powder blue")
        lblPRN_No.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,textvariable=self.prn_var,font=("arial",13,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="Title",padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,textvariable=self.id_var,font=("arial",13,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,font=("arial",12,"bold"),text="FirstName",padx=2,pady=6,bg="powder blue")
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,textvariable=self.firstname_var,font=("arial",13,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lastname",padx=2,pady=6,bg="powder blue")
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,textvariable=self.lastnane_var,font=("arial",13,"bold"),width=29)
        txtLastName.grid(row=4,column=1)

        lblAdress1=Label(DataFrameLeft,font=("arial",12,"bold"),text="Adress1",padx=2,pady=6,bg="powder blue")
        lblAdress1.grid(row=5,column=0,sticky=W)
        txtAdress1=Entry(DataFrameLeft,textvariable=self.address1_var,font=("arial",13,"bold"),width=29)
        txtAdress1.grid(row=5,column=1)

        lblAdress2=Label(DataFrameLeft,font=("arial",12,"bold"),text="Adress2",padx=2,pady=6,bg="powder blue")
        lblAdress2.grid(row=6,column=0,sticky=W)
        txtAdress2=Entry(DataFrameLeft,textvariable=self.address2_var,font=("arial",13,"bold"),width=29)
        txtAdress2.grid(row=6,column=1)

        lblPostcode=Label(DataFrameLeft,font=("arial",12,"bold"),text="Postcode",padx=2,pady=6,bg="powder blue")
        lblPostcode.grid(row=7,column=0,sticky=W)
        txtPostcode=Entry(DataFrameLeft,textvariable=self.postcode_var,font=("arial",13,"bold"),width=29)
        txtPostcode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,font=("arial",12,"bold"),text="Mobile",padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,textvariable=self.mobile_var,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=8,column=1)
      
        lblBookId=Label(DataFrameLeft,font=("arial",12,"bold"),text="bookId",padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLeft,textvariable=self.bookid_var,font=("arial",13,"bold"),width=29)
        txtBookId.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,font=("arial",12,"bold"),text="BookTitle",padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,textvariable=self.booktitle_var,font=("arial",13,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAutherName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Auther Name",padx=2,pady=6,bg="powder blue")
        lblAutherName.grid(row=2,column=2,sticky=W)
        txtAutherName=Entry(DataFrameLeft,textvariable=self.auther_var,font=("arial",13,"bold"),width=29)
        txtAutherName.grid(row=2,column=3)

        lblDateBorrowed=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Borrowed",padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,textvariable=self.dateborrowed_var,font=("arial",13,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date Due",padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,textvariable=self.datedue_var,font=("arial",13,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDateOnBook=Label(DataFrameLeft,font=("arial",12,"bold"),text="Date On Book",padx=2,pady=6,bg="powder blue")
        lblDateOnBook.grid(row=5,column=2,sticky=W)
        txtDateOnBook=Entry(DataFrameLeft,textvariable=self.daysonbook_var,font=("arial",13,"bold"),width=29)
        txtDateOnBook.grid(row=5,column=3)

        lblLateReturnfine=Label(DataFrameLeft,font=("arial",12,"bold"),text="LateReturnfine",padx=2,pady=6,bg="powder blue")
        lblLateReturnfine.grid(row=6,column=2,sticky=W)
        txtLateReturnfine=Entry(DataFrameLeft,textvariable=self.latereturnfine_var,font=("arial",13,"bold"),width=29)
        txtLateReturnfine.grid(row=6,column=3)

        lblDataOverdate=Label(DataFrameLeft,font=("arial",12,"bold"),text="DataOverdate",padx=2,pady=6,bg="powder blue")
        lblDataOverdate.grid(row=7,column=2,sticky=W)
        txtDataOverdate=Entry(DataFrameLeft,textvariable=self.dateoverdue_var,font=("arial",13,"bold"),width=29)
        txtDataOverdate.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="ActualPrice",padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,textvariable=self.finallprice_var,font=("arial",13,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

        
        #------------------------data from right---------------------------------------

        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="green",bd=12,relief=RIDGE,font=("time new roman",12,"bold"))
        DataFrameRight.place(x=860,y=5,width=530,height=360)

        self.txtBox=Text(DataFrameRight, font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Head First Book','Learn Python The Hard Way','Python Programming','Secrete Rahshy','Python CookBook','Into to Machine Lear','Fluent Python',
                   'programming Pyhon','The Algorithm','The tecnich Python',
                   'Machine tecno', 'My Python', 'Joss Elli guru', 'Elite Jungle python','Machine python', 'Advance Python', 
                   'Inton Python', 'RedChilli Python', 'Ishq Python']
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection()))
            x=value
            if (x=="Head First Book"):
                self.bookid_var.set("SKID5454")
                self.booktitle_var.set("Python Manual")
                self.auther_var.set("Paul Berry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.788")

            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic Of Python")
                self.auther_var.set("ZED A.SHAW")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.725")


            elif (x=="Python Programming"):
                self.bookid_var.set("BKID1245")
                self.booktitle_var.set("Intro to Python Comp Science")
                self.auther_var.set("John Zhelle")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.500")

               
            elif (x=="Secrete Rahshy"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Basic Of Python")
                self.auther_var.set("Ref.Kapil Kamble")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.289")

            elif (x=="Python CookBook"):
                self.bookid_var.set("BKID9348")
                self.booktitle_var.set("Basic Of nature")
                self.auther_var.set("Kapil Kamble")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.35")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.300")

            elif (x=="Fluent Python"):
                self.bookid_var.set("BKID2546")
                self.booktitle_var.set("Pthon cookbook")
                self.auther_var.set("Brain Jones")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.354")

            elif(x=="Into to Machine Lear"):
                self.bookid_var.set("BKID8796")
                self.booktitle_var.set("Intro to Machin Learning")
                self.auther_var.set("Paul Berry")
                d1=datetime.date.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set("15")
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finallprice_var.set("Rs.725")


        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
               listBox.insert(END,item)

        #-------------------------buttons frame-------------------------------------

        framebutton = Frame(self.root,bd=12,relief = RIDGE,padx=20,bg="powder blue")
        framebutton.place(x=0,y=530,width=1440,heigh=70)

        btnAddData=Button(framebutton,command=self.adda_data,text="Add Data",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(framebutton,command=self.showData,text="Show data",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(framebutton,command=self.update,text="Update",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(framebutton,command=self.delete,text="Delete",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(framebutton,command=self.reset,text="reset",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=4)

        btnAddData=Button(framebutton,command=self.iExit,text="Exit",font=("arial",12,"bold"),width=22,bg="blue",fg="white")
        btnAddData.grid(row=0,column=5)


        #-------------------------information frame---------------------------------

        FrameDetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0,y=590, width=1440,height=240)

        Table_frame=Frame (FrameDetails, bd=6, relief=RIDGE, bg="powder blue")
        Table_frame.place(x=0,y=2, width=1380,height=200)

        xscroll=ttk.Scrollbar (Table_frame, orient=HORIZONTAL)
        yscroll=ttk.Scrollbar (Table_frame, orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame, column=("memebertype", "prnno", "title", "firtname", "lastname", 
                                                            "adress1", "adress2", "postid", "mobile", "bookid", "booktitle", "auther",
                                                             "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X) 
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("memebertype", text="Member Type")
        self.library_table.heading("prnno", text="Reference No.")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firtname", text="Firstname")
        self.library_table.heading("lastname", text="Lastname")
        self.library_table.heading("adress1", text="Address1")
        self.library_table.heading("adress2", text="Address2")
        self.library_table.heading("postid", text="Post ID")
        self.library_table.heading("mobile", text="Mobile Number")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("auther", text="Auther")
        self.library_table.heading("dateborrowed", text="Date Of Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")



        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("memebertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title", width=100)
        self.library_table.column("firtname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100) 
        self.library_table.column("booktitle", width=100)
        self.library_table.column("auther", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100) 
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)


    def adda_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password= "satyajit", database= "collage")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastnane_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finallprice_var.get() ))
        
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success", "Member Has been Inserted successfull")

    def update(self):
        conn=mysql.connector.connect(host="localhost", username="root", password= "satyajit", database= "instagram")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set member=%s,id=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postid=%s,mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed=%s,datedue=%s,dayasofbook=%s,latereturnfine=%s,deteoverdue=%s,finalprice=%s where PRN_NO=%S",(
        

            self.member_var.set(),
            self.id_var.set(),
            self.firstname_var.set(),
            self.lastnane_var.set(),
            self.finallprice_var.get(),
            self.address1_var.set(),
            self.address2_var.set(),
            self.postcode_var.set(),
            self.mobile_var.set(), 
            self.bookid_var.set(),
            self.booktitle_var.set(),
            self.auther_var.set(),
            self.dateborrowed_var.set(),
            self.datedue_var.set(),
            self.daysonbook_var.set(),
            self.latereturnfine_var.set(),
            self.dateoverdue_var.set(),
            self.finallprice_var.set()))
        conn.commit()
        self.fatch_data()
        conn.close()
        messagebox.showinfo("Success","Member Has been inserted successfully")


    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password= "satyajit", database= "collage")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from data")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
           self.library_table.delete(*self.library_table.get_children())
           for i in rows:
            self.library_table.insert("",END,values=i)
           conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.libray_table.focus()
        content=self.libray_table.item(cursor_row)
        row=content['value']


        self.member_var.set(row[0])        
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastnane_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]), 
        self.booktitle_var.set(row[18]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finallprice_var.set(row[17]) 

    def showData(self):
        self.txtBox.insert(END,"member type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END, "PRN No:\t\t"+ self.prn_var.get() + "\n")
        self.txtBox.insert(END,"ID No: \t\t"+ self.id_var.get()+"\n")
        self.txtBox.insert(END,"Firstlane: \t\t"+ self.firstname_var.get() + "\n")
        self.txtBox.insert(END,"Lasthane:\t\t"+ self.lastnane_var.get() + "\n")
        self.txtBox.insert(END,"Address1\t\t"+ self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+ self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+ self.mobile_var.get() + "\n") 
        self.txtBox.insert(END,"Post Code:\t\t"+ self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+ self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Auther:\t\t"+ self.auther_var.get()+"\n")
        self.txtBox.insert(END,"Datellorrowed: \t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue:\t\t"+ self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook: \t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateRatefine:\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"Final Price:\t\t"+self.finallprice_var()+"\n")


    def reset(self):
        self.member_var.set(),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""), 
        self.lastnane_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""), 
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finallprice_var.set("")
        self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return        

    
    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Selct the Member")
        else: 
            conn=mysql.connector.connect(host="localhost", username="root", password= "satyajit", database= "instagram")
            my_cursor=conn.cursor()
            query="delete from library where PRN_NO=%s"
            value=(self.prn_var.get())
            my_cursor.execute(query,value)

            conn.commit
            self.fatch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success","Memmber has been Deleted")        
        

            


if __name__=="__main__":
            root=Tk()
            obj=LibraryManagementSystem(root)
            root.mainloop()
