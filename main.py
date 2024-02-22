from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector
 

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1540x800+0+0")
        
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose = StringVar()
        self.NumbersofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowtouseMedication = StringVar()
        self.patientID = StringVar()
        self.nhsNumber = StringVar()
        self.patientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()


        # font of hospital managemnet system
        
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text='HOSPITAL MANAGEMENT SYSTEM',fg='red',bg='white',font=('time new roman',50,'bold'))
        lbltitle.pack(side=TOP,fill=X)
        
        
        
        #  dataframe
        Dataframe = Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        # dataframeleft
        
        Dataframeleft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Patient Information")
        Dataframeleft.place(x=0,y=5,width=980,height=350)
        
        
        # dataframeright
        
        Dataframeright = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("arial",12,"bold"),text="Prescription")
        Dataframeright.place(x=990,y=5,width=460,height=350)
        
        # buttons frame
        
        Buttonframe=Frame(self.root,bd=18,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=100)
        
        
        # Details frame
        
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        
        # dataframe left
        lbltitleTablet = Label(Dataframeleft,text='Names uf tablet',font=('arial',12,'bold'),padx=2,pady=6)        
        lbltitleTablet.grid(row=0,column=0)
        
        comNametablet = ttk.Combobox(Dataframeleft,textvariable=self.Nameoftablets,state="readonly",font=('arial',12,'bold'),width=33)
        
        comNametablet['values'] = ('Nice','corona Vacacine','Acetaminphne','Adderall','Amlodipine','Ativan')
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)
        
        lblref = Label(Dataframeleft,font=('arial',12,'bold'),text='Refence No:',padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        
        lblDose = Label(Dataframeleft,font=('arial',12,'bold'),text='Dose:',padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)
        
        
        lblNoOftablets = Label(Dataframeleft,font=('arial',12,'bold'),text='No of tablets:',padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.NumbersofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        
        lblLot = Label(Dataframeleft,font=('arial',12,'bold'),text='Lot:',padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        
        lblissueDate = Label(Dataframeleft,font=('arial',12,'bold'),text='Issue Date:',padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)
        
        
        lblExpDate = Label(Dataframeleft,font=('arial',12,'bold'),text='Expire Date:',padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtexpDate = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.Expdate,width=35)
        txtexpDate.grid(row=6,column=1)
        
                
        lblDailyDose = Label(Dataframeleft,font=('arial',12,'bold'),text='Daily Dose:',padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
        
        
        lblSideEffect = Label(Dataframeleft,font=('arial',12,'bold'),text='Side Effect:',padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)
        
        
        lblFurtherinfo = Label(Dataframeleft,font=('arial',12,'bold'),text='Further Information:',padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        
        lblDrivingMachine = Label(Dataframeleft,font=('arial',12,'bold'),text='Blood Pressure:',padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.DrivingUsingMachine,width=35)
        txtDrivingMachine.grid(row=1,column=3)
        
        
        
        lblStorage = Label(Dataframeleft,font=('arial',12,'bold'),text='Storage:',padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)
        
        
        lblMedicine = Label(Dataframeleft,font=('arial',12,'bold'),text='Medicine:',padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(Dataframeleft,font=('arial',13,'bold'),textvariable=self.HowtouseMedication,width=35)
        txtMedicine.grid(row=3,column=3)
        
        
        lblPatientId = Label(Dataframeleft,font=('arial',12,'bold'),text='PatientId:',padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId = Entry(Dataframeleft,font=('arial',12,'bold'),textvariable=self.patientID,width=35)
        txtPatientId.grid(row=4,column=3)
        
        
        lblNhsNumber = Label(Dataframeleft,font=('arial',12,'bold'),text='NHS Number:',padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(Dataframeleft,font=('arial',12,'bold'),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        
        lblPatientNme = Label(Dataframeleft,font=('arial',12,'bold'),text='Patient Name:',padx=2,pady=6)
        lblPatientNme.grid(row=6,column=2,sticky=W)
        txtPatientname = Entry(Dataframeleft,font=('arial',12,'bold'),textvariable=self.patientName,width=35)
        txtPatientname.grid(row=6,column=3)
        
        
        lblDataOfBirth = Label(Dataframeleft,font=('arial',12,'bold'),text='Data Of Birth:',padx=2,pady=6)
        lblDataOfBirth.grid(row=7,column=2,sticky=W)
        txtDataOfBirth = Entry(Dataframeleft,font=('arial',12,'bold'),textvariable=self.DateOfBirth,width=35)
        txtDataOfBirth.grid(row=7,column=3)
        
        
        lblPatientAddress = Label(Dataframeleft,font=('arial',12,'bold'),text='Patient Address:',padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(Dataframeleft,font=('arial',12,'bold'),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        
        # dataframe right
        self.txtprescription = Text(Dataframeright,font=('arial',12,'bold'),width=48,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

    
        
        # buttons

        btnprescription = Button(Buttonframe,command=self.iprectioption, text="prescription", bg='yellow', fg="white", font=('arial', 12, 'bold'), width=23, height=16, padx=2, pady=6)
        btnprescription.grid(row=0, column=0)
        
        
        btnprescritionData = Button(Buttonframe,text="prescription Data",bg="green",fg="white",font=('arial',12,'bold') ,width=23,height=16,padx=2,pady=6 ,command=self.iprescriptionData)
        btnprescritionData.grid(row=0,column=1)
       
        
        btnUpdate = Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=('arial',12,'bold'),width=23,height=16,padx=2,pady=6 )
        btnUpdate.grid(row=0,column=2)
        
        
        btnDelete = Button(Buttonframe,command=self.idelect,text="Delete",bg="green",fg="white",font=('arial',12,'bold') ,width=23,height=16,padx=2,pady=6 )
        btnDelete.grid(row=0,column=3)
        
        
        btnClear = Button(Buttonframe,command=self.clear ,text="Clear",bg="green",fg="white",font=('arial',12,'bold') ,width=23,height=16,padx=2,pady=6 )
        btnClear.grid(row=0,column=4)
        
        
        btnExit = Button(Buttonframe,command=self.iExit,text="=Exit",bg="green",fg="white",font=('arial',12,'bold') ,width=23,height=16,padx=2,pady=6 )
        btnExit.grid(row=0,column=5)
        
        
        
        
        # table
        
        #  scrollbar
       
        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hosptital_table = ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hosptital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hosptital_table.yview)
        
        
        self.hosptital_table.heading("nameoftable", text="Name of the table")
        self.hosptital_table.heading("ref",text="reference No.")
        self.hosptital_table.heading("dose",text="Dose")
        self.hosptital_table.heading("nooftablets",text="No of Tablets")
        self.hosptital_table.heading("lot",text="Lot")
        self.hosptital_table.heading("issuedate",text="Issue Date")
        self.hosptital_table.heading("expdate",text="Issue Date")
        self.hosptital_table.heading("dailydose",text="Dailty Dose")
        self.hosptital_table.heading("storage",text="Storage")
        self.hosptital_table.heading("nhsnumber",text="NHS number")
        self.hosptital_table.heading("pname",text="Patient Number")
        self.hosptital_table.heading("dob",text="DOB")
        self.hosptital_table.heading("address",text="Address")
        
        self.hosptital_table["show"]="headings"
      
        
        self.hosptital_table.column("nameoftable",width=100)
        self.hosptital_table.column("ref",width=100)
        self.hosptital_table.column("dose",width=100)
        self.hosptital_table.column("nooftablets",width=100)
        self.hosptital_table.column("lot",width=100)
        self.hosptital_table.column("issuedate",width=100)
        self.hosptital_table.column("expdate",width=100)
        self.hosptital_table.column("dailydose",width=100)
        self.hosptital_table.column("storage",width=100)
        self.hosptital_table.column("nhsnumber",width=100)
        self.hosptital_table.column("pname",width=100)
        self.hosptital_table.column("dob",width=100)
        self.hosptital_table.column("pname",width=100)
        
        
          
        self.hosptital_table.pack(fill=BOTH,expand=1)
        self.hosptital_table.bind('<ButtonRelease-1>',self.get_cursor)
        self.fetch_data()



    #Functionlity Declration
    def iprescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror('error','All field are required')
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='root@12',database='mydata')
            my_cursor=conn.cursor()
            my_cursor.execute('insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                       
                                                                                                       self.Nameoftablets.get(),
                                                                                                       self.ref.get(),
                                                                                                       self.Dose.get(),
                                                                                                       self.NumbersofTablets.get(),
                                                                                                       self.Lot.get(),
                                                                                                       self.Issuedate.get(),
                                                                                                       self.Expdate.get(),
                                                                                                       self.DailyDose.get(),
                                                                                                       self.StorageAdvice.get(),
                                                                                                       self.nhsNumber.get(),
                                                                                                       self.patientName.get(),
                                                                                                       self.DateOfBirth.get(),
                                                                                                       self.PatientAddress.get()
                                                                                                       ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo('success','recod has been inserted')
            
    
    def update_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root@12',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital  set Nameoftablets=%s, dose=%s, Numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOS=%s, patientaddress=%s  where  Reference_No=%s",(
                                                                                                       
                                                                                                       self.Nameoftablets.get(),
                                                                                                       self.Dose.get(),
                                                                                                       self.NumbersofTablets.get(),
                                                                                                       self.Lot.get(),
                                                                                                       self.Issuedate.get(),
                                                                                                       self.Expdate.get(),
                                                                                                       self.DailyDose.get(),
                                                                                                       self.StorageAdvice.get(),
                                                                                                       self.nhsNumber.get(),
                                                                                                       self.patientName.get(),
                                                                                                       self.DateOfBirth.get(),
                                                                                                       self.PatientAddress.get(),
                                                                                                       self.ref.get()
                                                                                                       ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo('success','recod has been updated')
        
    
    
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root@12',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.hosptital_table.delete(*self.hosptital_table.get_children())
            for i in rows:
                self.hosptital_table.insert('',END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row = self.hosptital_table.focus()
        content = self.hosptital_table.item(cursor_row)
        row=content['values']
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumbersofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.patientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
    def iprectioption(self):
        self.txtprescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get() + "\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t"+self.ref.get() + "\n")
        self.txtprescription.insert(END,"Dose:\t\t\t"+self.Dose.get() + "\n")
        self.txtprescription.insert(END,"Number of Tablets:\t\t\t"+self.NumbersofTablets.get() + "\n")
        self.txtprescription.insert(END,"Lot:\t\t\t"+self.Lot.get() + "\n")
        self.txtprescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get() + "\n")
        self.txtprescription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get() + "\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get() + "\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get() + "\n")
        self.txtprescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get() + "\n")
        self.txtprescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get() + "\n")
        self.txtprescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get() + "\n")
        self.txtprescription.insert(END,"Patient ID:\t\t\t"+self.patientID.get() + "\n")
        self.txtprescription.insert(END,"NHSnumber:\t\t\t"+self.nhsNumber.get() + "\n")
        self.txtprescription.insert(END,"patientName:\t\t\t"+self.patientName.get() + "\n")
        self.txtprescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get() + "\n")
        self.txtprescription.insert(END,"patient Address:\t\t\t"+self.PatientAddress.get() + "\n")
        
    def idelect(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='root@12',database='mydata')
        my_cursor=conn.cursor()
        query = 'delete from hospital where Reference_No=%s'
        Value=(self.ref.get(),)
        my_cursor.execute(query,Value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo('delect','patient has been delected successfully')
        
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumbersofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowtouseMedication.set("")
        self.patientID.set("")
        self.nhsNumber.set("")
        self.patientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtprescription.delete("1.0",END)
        
        
    def iExit(self):
        iexit=messagebox.askyesno("hopsital managment system ","confirm you want to exit")
        if iexit > 0:
            root.destroy()
            return
        
        
        




       

        
        
        
        
        
        
        
     

        

    
    
    
       




root=Tk()
ob=Hospital(root)
root.mainloop()